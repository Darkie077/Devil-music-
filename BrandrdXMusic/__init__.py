from RenXMusic.core.bot import Hotty
from RenXMusic.core.dir import dirr
from RenXMusic.core.git import git
from RenXMusic.core.userbot import Userbot
from RenXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
