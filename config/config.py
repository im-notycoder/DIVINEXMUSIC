import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

#❖ Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "27577004"))
API_HASH = getenv("API_HASH", "b6ba627b943a1e03ad76cc2d294e5863")

#❖ Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME", "FondOfYouuBabe")

#❖  Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME", "DivineMusicXBot")

#❖  Don't Add style font 
BOT_NAME = getenv("BOT_NAME", "𝑫𝒚𝒏𝒂𝒎𝒊𝒄 ✗ 𝑴𝒖𝒔𝒊𝒄™")

#❖ get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME", "𝑫𝒚𝒏𝒂𝒎𝒊𝒄 ✗ 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕")

#❖ Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7717606847:AAEfG3DctNNxPfjMZiBx-avZdhC1yJELIuE")

#❖ Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Mafia:Mafia@mafia.wvuzxgl.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600000))

#❖  Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002093750764"))

#❖ Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7841940691"))

#❖  Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

#❖  Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/im-notycoder/DIVINEXMUSIC",
)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  #❖ Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DynamicXNetwork")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DynamicXSupport")

#❖ Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


#❖ Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "e319091f771445b18c029299505d5d4f")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "293c334a2861415197a697b2d11dd4de")


#❖ Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


#❖ Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
#❖ Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


#❖ Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGkyqwAS77k_H-xTA-TxvV1SKgu5mpjOdBeMIr1KpKVH8SXGQGgY6f98uSWirk3gP-xq3iYMTz9eZ2RwqNn6FnjdgRM3xv0J24h8BdWPwx0KB3jabl_AwbocMT8fenyRvXbhPI7CN9mvrrdhhsaNyPGC8TuzM8NQMQqmy9gi2FRRaRr176tae1MYVXfYU1AZXuGVtxrpZ4X4TnWSMmjZlcn8BWqCfTACDVaPql2a8qGihIZlU43NWr4t-_lhB2zxoeTbv0nSn1Dj-p5sJxUnxOKiKpzZl13db5x0sEPIkFdgT2jr_qHeTO3T2m31qZ1Yhk8JhJqC4DkfF3sGaSxrkDnXmjTPAAAAAHl3gl2AA")
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
    "START_IMG_URL", "https://files.catbox.moe/ek09al.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/ywsxz7.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/7795e58425337d0455e95.jpg"
STATS_IMG_URL = "https://i.ibb.co/xmxBfGm/photo-2024-11-19-14-16-17-7438994282792353840.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"



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
