import praw
from config import *


def post(title: str, img_path='Squad.png', subreddit='joinsquad'):
    r = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
        user_agent='used to post 1 ticket wins to r/joinsquad'
    )

    r.subreddit(subreddit).submit_image(title, img_path)
