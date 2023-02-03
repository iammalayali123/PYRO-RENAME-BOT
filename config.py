import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24775692")

API_HASH = os.environ.get("API_HASH", "f636880465005ae028ea42fc215d963b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6199152329:AAEyKua2Nt81fVuz11ncegFS_CAzPrhaJJQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","iammalayali")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Iammalayali123:iammalayali@cluster0.defpuhd.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

