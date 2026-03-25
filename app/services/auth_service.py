import hashlib
import os


class AuthService:
    # save the credentials in a dictionary in format of salt and hashed password
    #the salt is used to make the password more secure.
    def __init__(self):
        self._credentials: dict[str, tuple[str, str]] = {}  # user_id -> (salt, hashed_password)

        # saves the session tokens in a dictionary
        self._tokens: dict[str, str] = {}  # token -> user_id

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
