from instabot import Bot

import time


# Function to retrieve the list of friends with rate limiting
def get_friends_list_with_rate_limit(username, password):
    bot = Bot()
    bot.login(username=username, password=password)

    friends_list = {}
    friends = bot.get_user_following(username)

    # Delay between requests to comply with rate limits
    time.sleep(10)  # Adjust the delay as needed

    for friend in friends:
        friends_list[friend] = bot.get_user_info(friend)['full_name']

        # Delay between requests to comply with rate limits
        time.sleep(5)  # Adjust the delay as needed

    return friends_list


def save_friends_list_to_file(friends_list, file_path):
    with open(file_path, 'w') as file:
        file.write("friends_list = ")
        file.write(repr(friends_list))


def main():
    # Replace with your Instagram username and password
    instagram_username = "maymays.wtf"
    instagram_password = "maymays@123"

    # Retrieve friends list
    friends = get_friends_list_with_rate_limit(instagram_username, instagram_password)
    print("Friends List:")
    for username, full_name in friends.items():
        print(f"{username}: {full_name}")

    # Save friends list to a Python file
    file_path = "friends.py"
    save_friends_list_to_file(friends, file_path)
    print(f"Friends list saved to {file_path}")


main()
