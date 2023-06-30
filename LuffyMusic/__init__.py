from LuffyMusic.core.bot import LuffyXbot
from LuffyMusic.core.dir import dirr
from LuffyMusic.core.git import git
from LuffyMusic.core.userbot import Userbot
from LuffyMusic.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = LuffyMusicBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
