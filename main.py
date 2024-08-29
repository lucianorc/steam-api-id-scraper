from steamdb.repositories.user import UserRepository


mat_user = "76561198043967700"
my_user = "76561198193901450"

if __name__ == "__main__":
    user_repo = UserRepository()
    user = user_repo.get_user(my_user)
    print(user)
    # print(json.dumps(user))
