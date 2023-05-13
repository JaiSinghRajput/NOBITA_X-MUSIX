from nobitaX.core.bot import nobitaXBot
from nobitaX.core.dir import dirr
from nobitaX.core.git import git
from nobitaX.core.userbot import Userbot
from nobitaX.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = nobitaXBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
