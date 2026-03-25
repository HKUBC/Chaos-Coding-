class AuthService:
    def __init__(self):
        self._credentials: dict[str, str] = {}  # user_id -> password | basic logic


    #simple funcitons to sign up and login
    def sign_up(self, user_id: str, password: str) -> None:
        if user_id in self._credentials:
            raise ValueError(f"User {user_id} already has an account.")
        self._credentials[user_id] = password

    def login(self, user_id: str, password: str) -> str:
        if user_id not in self._credentials:
            raise ValueError(f"No account found for {user_id}.")
        if self._credentials[user_id] != password:
            raise ValueError("Incorrect password.")
        return user_id
