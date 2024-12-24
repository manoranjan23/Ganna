import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "8060061"))

API_HASH = getenv("API_HASH", "0a19238a019c119cea065eae38cebcd2")

BOT_TOKEN = getenv("BOT_TOKEN", "7312074776:AAESKL9QWisPkrjCyZ6B0a9u10A7NGfQKaw")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Somu:Somu@somu.xbkiklu.mongodb.net/?retryWrites=true&w=majority&appName=Somu")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", "-1002100433415"))

OWNER_ID = int(getenv("OWNER_ID", "7070591202"))

BOT_USERNAME = getenv("BOT_USERNAME" , "ISHU X MUSIC")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/manoranjan23/Ganna",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/somueditingzone")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/somueditingzone")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "BQB6_J0AAb6mb69WZ0-m6E847-Pao_ikLMYGzM3su_7XG6IOjuqjLJd-HmYp3_HD6NPDoTeve7oNeNpQQxUj0dcuITKz4LOgOgstLZg8-gJCVGLKoGhAzeNXCVqSxmqNw9mmmpxzdg3YndP8xSaEQ65ZntU9UJ3YXv9dRkHTLI-So1cnY1Sfa4Bz-GWPkTwAdUVxOSz8AAaM3vYGAN0hIsm_M-IAn3vmSAhykifVto8yKjxp9bnEVD7AqRc3qqQzzdv422JZSWZV5jlO2dGWOSYabSh8A0CWol3bAOKl9y2hwvT7YbDawZVNFOGk3ImvS9SFDH9-Mhi3KsIAWaPAHQQsqEWCegAAAAFq-q5XAA")
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
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/JBB.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/7wc.jpg"
)
PLAYLIST_IMG_URL = "https://iili.io/2uvE6Cl.md.jpg"
STATS_IMG_URL = "https://envs.sh/JWK.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/a834c4bd7bbe22f55a475.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/dd84a3ccf42bead1a203a.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/590f5404cdc7840b63a1c.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/a90f5510f264e403e3cb9.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

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
