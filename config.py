import os
   
PREFIXES = ['!', '/', '$']
   
OWNER_ID = os.getenv("OWNER_ID", 1238234357)
SUDO_USERS = os.getenv("SUDO_USERS", 6916220465, 7370080350)
HANDLER = [".", "!", "/", "$"]
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "-1001862411671")
LOGS_CHAT = -1001862411671
