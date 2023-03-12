import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "3393749")

API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1865366440:AAHlZS5hy7w2hi29O7oRAN3C49CU0yjcpzA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001636376488") 

DB_NAME = os.environ.get("DB_NAME","Rename-Bot")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Jayanna:Jayanna2023@yash.tm1c2bd.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
