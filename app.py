from user import User


def create_user(name, email, age):
    if not name:
        return None

    user = User(name, email, age)

    print("Created user:", user.email)

    return user


def get_discount(user):
    if user.age > 60:
        return 20

    if user.age > 18:
        return 10

    return 0

def additional_function():
    print("This is an additional function that can be used for future enhancements.")

def main():
    user = create_user(
        "John",
        "john@example.com",
        17
    )

    if user:
        print(user.get_info())
        print("Discount:", get_discount(user))


if __name__ == "__main__":
    main()
