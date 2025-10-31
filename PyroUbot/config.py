import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "7197652621").split()))

API_ID = int(os.getenv("API_ID", "24826363"))

API_HASH = os.getenv("API_HASH", "2ae8707e6c3fbc7981f884e3f95c79f1")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8316005905:AAGmETstj-tmV92-U29XNsCOAovR5tpLLKw")

OWNER_ID = int(os.getenv("OWNER_ID", "7197652621"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002886184276").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("mongodb+srv://ryuzo:Hanzz7308@cluster0.j0jxvhq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002671518601"))
