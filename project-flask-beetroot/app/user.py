from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        self.remember_me = False
        self.is_active = True
        self.is_authenticated = False

    def get_id(self):
        return self.id

    def set_password(self):
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        return check_password_hash(self.password, password)