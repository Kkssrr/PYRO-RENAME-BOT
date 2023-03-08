import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "11604258")

API_HASH = os.environ.get("API_HASH", "447e00413945ab1a61882f9e474477d6")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5517278922:AAETx0EGT2v84--UB1Nk2uRRPtvfHoTQYO8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-100178537297") 

DB_NAME = os.environ.get("DB_NAME","Real")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Real:QICMgfw8fdbfst41@cluster0.i4idyao.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2027727486').split()]

PORT = os.environ.get('PORT', '8080')
