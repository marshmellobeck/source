import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "marshmello_30")
ALIVE_NAME = getenv("ALIVE_NAME", "『×˹MARSH₍꯭🇬🇧⁾MELLO͓˼×』")
BOT_USERNAME = getenv("BOT_USERNAME", "ME_LLO_MUSICBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ME_LL_O")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "bar_mello")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "mr_marshmello30")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/marshmellobeck/source")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/30452a15a60e0f95c5688.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
