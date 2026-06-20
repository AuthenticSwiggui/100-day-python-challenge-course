class User:

    #Initializes the class, also knnown as Constructor
    def __init__(self, user_id, username):
        print("Creating new user.....")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        print(f"Following {user.username}")
        user.followers += 1
        self.following += 1

def print_follows(user) -> None:
    print(f"Followers: {user.followers}")
    print(f"Followers: {user.following}")

user_01 = User("1", "Angela")
user_02 = User("2", "Jack")

print_follows(user_02)


user_01.follow(user_02)

print_follows(user_02)


