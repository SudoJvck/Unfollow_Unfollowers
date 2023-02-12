import tweepy

def get_input(prompt):
    return input(prompt).strip()

consumer_key = get_input("Enter your Twitter Consumer Key: ")
consumer_secret = get_input("Enter your Twitter Consumer Secret: ")
access_token = get_input("Enter your Twitter Access Token: ")
access_token_secret = get_input("Enter your Twitter Access Token Secret: ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

followers = api.followers()

friends = api.friends()

unfollowers = [friend for friend in friends if friend not in followers]

for unfollower in unfollowers:
    api.destroy_friendship(unfollower.id)
