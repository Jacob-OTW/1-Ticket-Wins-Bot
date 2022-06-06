from image import create_image, grab_random_image
from post import post

Images = [
    grab_random_image('images/maps/'),
    grab_random_image('images/overlay/')
]

create_image(Images)

print()
# post('Look at this crazy 1 ticket win!', subreddit='U_1-Ticket-Wins')
