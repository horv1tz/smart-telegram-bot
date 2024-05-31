from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.environ.get("BOT_TOKEN")
SBER_AUTH_DATA = os.environ.get("SBER_AUTH_DATA")
SBER_TOKEN = os.environ.get("SBER_TOKEN")

# allowed_urls = ["wikipedia.org", "habr.com", "dzen.ru", "vk.com", "2gis.ru", "krasnoeibeloe.ru", "python.org", "pipy.", "pypi.org", "github.com", "yandex.ru", "pythontutor.ru"]
allowed_urls = []

