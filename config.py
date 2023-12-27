import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24173620")

API_HASH = os.environ.get("API_HASH", "35709a710e33be401047f08d0199b82b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "35709a710e33be401047f08d0199b82b") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001928530174") 

DB_NAME = os.environ.get("DB_NAME","jaypal_thakor_148")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://jaypal_thakor_148:jaypal.008@mk40@atlascluster.fmnvlon.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/b1f145b52a2341c4db7d3.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5494468015').split()]

PORT = os.environ.get("PORT", "8080")
