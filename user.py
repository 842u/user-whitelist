import csv

class User:
    user_list = []

    @classmethod
    def instantion_from_whitelist(cls):
        User.user_list.clear()

        with open('whitelist.csv', 'r') as f:
            reader = csv.DictReader(f)
            users = list(reader)

        for user in users:
            User(
                index = user.get('index'),
                name = user.get('name'),
                password = user.get('password'),
                email = user.get('email')
            )

    def __init__(self, index="", name="", password="", email="") -> None:
        self.index = index
        self.name = name
        self.password = password
        self.email = email

        User.user_list.append(self)
