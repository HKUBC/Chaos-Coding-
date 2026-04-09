import hashlib
import os
from app.model.user_role import UserRole


class AuthService:
    # save the credentials in a dictionary in format of salt and hashed password
    #the salt is used to make the password more secure.
    def __init__(self):
        self._credentials: dict[str, tuple[str, str]] = {}  # user_id -> (salt, hashed_password)
        self._roles: dict[str, UserRole] = {}               # user_id -> role
        self._restaurant_ids: dict[str, int] = {}           # user_id -> restaurant_id (owners only)

        # saves the session tokens in a dictionary
        self._tokens: dict[str, str] = {}  # token -> user_id

# the sha256 is an alogrithm that is used to hast the password.
    def _hash_password(self, password: str, salt: str) -> str:
        return hashlib.sha256((salt + password).encode()).hexdigest()

# os.urandom is used to generate a random salt for each user
    def sign_up(self, user_id: str, password: str, role: UserRole, restaurant_id: int | None = None) -> None:
        if user_id in self._credentials:
            raise ValueError(f"User {user_id} already has an account.")
        salt = os.urandom(16).hex()
        self._credentials[user_id] = (salt, self._hash_password(password, salt))
        self._roles[user_id] = role
        if restaurant_id is not None:
            self._restaurant_ids[user_id] = restaurant_id

    def login(self, user_id: str, password: str) -> str:
        if user_id not in self._credentials:
            raise ValueError(f"No account found for {user_id}.")
        salt, stored_hash = self._credentials[user_id]
        if self._hash_password(password, salt) != stored_hash:
            raise ValueError("Incorrect password.")
        # this creates a random token for the session and saves it
        token = os.urandom(32).hex()
        self._tokens[token] = user_id
        return token

 # this validates the token by checkin if it exists in dictionary
 # and then returns the user id associated with it
    def validate_token(self, token: str) -> str:
        if token not in self._tokens:
            raise ValueError("Invalid or expired session token.")
        return self._tokens[token]

#this deletes the token from the dictionary to logout the user
    def logout(self, token: str) -> None:
        if token not in self._tokens:
            raise ValueError("Invalid or expired session token.")
        del self._tokens[token]

    # returns the role of the user associated with the token
    def get_role(self, token: str) -> UserRole:
        user_id = self.validate_token(token)
        return self._roles[user_id]

    def get_me(self, token: str) -> dict:
        user_id = self.validate_token(token)
        return {
            "user_id": user_id,
            "role": self._roles[user_id].value,
            "restaurant_id": self._restaurant_ids.get(user_id)
        }

    # raises an error if the user's role does not match the required role
    def require_role(self, token: str, required_role: UserRole) -> None:
        if self.get_role(token) != required_role:
            raise ValueError(f"Access denied. Required role: {required_role.value}.")
