import hashlib
import os
import json
from app.model.user_role import UserRole


# Credentials are persisted to this file so logins survive server restarts
_DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'users.json')


class AuthService:
    def __init__(self):
        self._credentials: dict[str, tuple[str, str]] = {}  # user_id -> (salt, hashed_password)
        self._roles: dict[str, UserRole] = {}               # user_id -> role
        self._restaurant_ids: dict[str, int] = {}           # user_id -> restaurant_id (owners only)
        self._tokens: dict[str, str] = {}                   # token -> user_id
        self._profiles: dict[str, dict] = {}                # user_id -> {full_name, email, phone, ...}

        self._load()

    # ── Persistence ────────────────────────────────────────────────────────

    def _load(self) -> None:
        """Load saved users from disk on startup."""
        try:
            with open(_DATA_FILE, 'r') as f:
                data = json.load(f)
            for user_id, entry in data.items():
                self._credentials[user_id] = (entry['salt'], entry['hashed_password'])
                self._roles[user_id] = UserRole(entry['role'])
                if entry.get('restaurant_id') is not None:
                    self._restaurant_ids[user_id] = entry['restaurant_id']
                if entry.get('profile'):
                    self._profiles[user_id] = entry['profile']
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            pass  # First run or corrupted file — start fresh

    def _save(self) -> None:
        """Persist all users to disk."""
        data = {
            user_id: {
                'salt':            salt,
                'hashed_password': hashed,
                'role':            self._roles[user_id].value,
                'restaurant_id':   self._restaurant_ids.get(user_id),
                'profile':         self._profiles.get(user_id, {}),
            }
            for user_id, (salt, hashed) in self._credentials.items()
        }
        os.makedirs(os.path.dirname(_DATA_FILE), exist_ok=True)
        with open(_DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)

    # ── Core auth ──────────────────────────────────────────────────────────

    def _hash_password(self, password: str, salt: str) -> str:
        return hashlib.sha256((salt + password).encode()).hexdigest()

    def sign_up(self, user_id: str, password: str, role: UserRole,
                restaurant_id: int | None = None, profile: dict | None = None) -> None:
        if user_id in self._credentials:
            raise ValueError(f"Username '{user_id}' is already taken. Please try a different username.")
        salt = os.urandom(16).hex()
        self._credentials[user_id] = (salt, self._hash_password(password, salt))
        self._roles[user_id] = role
        if restaurant_id is not None:
            self._restaurant_ids[user_id] = restaurant_id
        if profile:
            self._profiles[user_id] = profile
        self._save()

    def login(self, user_id: str, password: str) -> str:
        if user_id not in self._credentials:
            raise ValueError(f"No account found for '{user_id}'.")
        salt, stored_hash = self._credentials[user_id]
        if self._hash_password(password, salt) != stored_hash:
            raise ValueError("Incorrect password.")
        token = os.urandom(32).hex()
        self._tokens[token] = user_id
        return token

    def validate_token(self, token: str) -> str:
        if token not in self._tokens:
            raise ValueError("Invalid or expired session token.")
        return self._tokens[token]

    def logout(self, token: str) -> None:
        if token not in self._tokens:
            raise ValueError("Invalid or expired session token.")
        del self._tokens[token]

    def get_role(self, token: str) -> UserRole:
        user_id = self.validate_token(token)
        return self._roles[user_id]

    def get_me(self, token: str) -> dict:
        user_id = self.validate_token(token)
        profile = self._profiles.get(user_id, {})
        return {
            "user_id": user_id,
            "role": self._roles[user_id].value,
            "restaurant_id": self._restaurant_ids.get(user_id),
            **profile,
        }

    def require_role(self, token: str, required_role: UserRole) -> None:
        if self.get_role(token) != required_role:
            raise ValueError(f"Access denied. Required role: {required_role.value}.")
