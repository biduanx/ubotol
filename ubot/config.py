import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [1838348402, 6051457085, 6696975845]



API_ID = int(os.getenv("API_ID", "20304260"))

API_HASH = os.getenv("API_HASH", "763e943987ee09ec449ad1611b7f5fc1")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7270284535:AAGh4Sxt9voXUgIZJIYHoAj4ixsVgK07H5s")

OWNER_ID = int(os.getenv("OWNER_ID", "1838348402"))

USER_ID = list(map(int, os.getenv("USER_ID", "6696975845 1838348402 6696975845 6051457085 6527347171").split()))

LOG_UBOT = int(os.getenv("LOG_UBOT", "-1002234875244"))

LOG_SELLER = int(os.getenv("LOG_SELLER", "-1002332295934"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002075041230 -1002164901876 -1002166018703 -1001473548283 -1001390552926 -1001672802736 -1001917973794 -1002433894643").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "sk-b76-2Xm3NudxolduxgQnvFQTmbSjF0MQEVXtP4EfmMT3BlbkFJfk1LYV_1GUrcanMhuvhafaJ2dLs4yYwsgH5aBtaI8A",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL", "mongodb+srv://yxxxgans:bt30ztfR9EYPAnV0@botme.srpuzxu.mongodb.net/?retryWrites=true&w=majority&appName=botme")
