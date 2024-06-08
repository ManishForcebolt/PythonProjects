class User:

    def __init__(self, userid, username):
        self.user_id = userid
        self.user_name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("001", "Manish")
user_2 = User("002", "Avinash")

user_1.follow(user_2)
user_2.follow(user_1)

print(user_1.following)
print(user_1.followers)
print(user_2.followers)
print(user_2.following)
