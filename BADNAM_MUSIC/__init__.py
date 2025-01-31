from BADNAM_MUSIC.core.bot import BADNAM
from BADNAM_MUSIC.core.dir import dirr
from BADNAM_MUSIC.core.git import git
from BADNAM_MUSIC.core.userbot import Userbot
from BADNAM_MUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = BADNAM()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
