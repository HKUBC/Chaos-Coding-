import hashlib
import os


class AuthService:
    # save the credentials in a dictionary in format of salt and hashed password
    #the salt is used to make the password more secure.
    def __init__(self):
        self._credentials: dict[str, tuple[str, str]] = {}  # user_id -> (salt, hashed_password)

# the sha256 is an alogrithm that is used to hast the password.
    def _hash_password(self, password: str, salt: str) -> str:
        return hashlib.sha256((salt + password).encode()).hexdigest()

# os.urandom is used to generate a random salt for each user
    def sign_up(self, user_id: str, password: str) -> None:
        if user_id in self._credentials:
            raise ValueError(f"User {user_id} already has an account.")
        salt = os.urandom(16).hex()
        self._credentials[user_id] = (salt, self._hash_password(password, salt))

    def login(self, user_id: str, password: str) -> str:
        if user_id not in self._credentials:
            raise ValueError(f"No account found for {user_id}.")
        salt, stored_hash = self._credentials[user_id]
        if self._hash_password(password, salt) != stored_hash:
            raise ValueError("Incorrect password.")
        return user_id
