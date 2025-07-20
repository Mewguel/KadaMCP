from dotenv import load_dotenv
import os

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

assert NOTION_TOKEN, "NOTION_TOKEN not set"
assert NOTION_DATABASE_ID, "NOTION_DATABASE_ID not set"