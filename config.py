import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", None)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @ren_music_bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6598102996))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Darkie077/Devil-music-",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/Cyber_sellers_TCE" getenv("SUPPORT_CHANNEL", "https://t.me/Cyber_sellers_TCE")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/thesupport3")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/5f3660a893e99a9f3651a.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/5f3660a893e99a9f3651a.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/fe0cf2142210df1f0c85d.jpg"
STATS_IMG_URL = "https://telegra.ph/file/5243f82e51c86aa6649e7.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/feae2b9dfe978ac487944.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/2a468a481b4d8aabb6f3a.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/95a72a593c34561cf6445.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/dc2fada397399560246f8.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/549591898c7c81e39248b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/39dae07cd003c263d4d69.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6bca0e731b81b0980cde0.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/e6d10496cbdb1bce1c4a5.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
