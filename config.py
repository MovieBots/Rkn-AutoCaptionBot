# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Rkn_Bots(object):
    
    # Rkn client config  ( required.. 😥)
    API_ID = os.environ.get("API_ID", "29236719")
    API_HASH = os.environ.get("API_HASH", "1ccf1bd0a86af974e3210a55f662c062")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # start_pic
    RKN_PIC = os.environ.get("RKN_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")

    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))

    # force subs channel ( required.. 😥)
    FORCE_SUB = os.environ.get("FORCE_SUB", "MOVIES_WORLDZSS") 
    
    # database config ( required.. 😥)
    DB_NAME = os.environ.get("DB_NAME", "AutoCaption_V05_Bot")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://keshavptdr98:D8lbdQUW4euV07l4@cluster0.dok926y.mongodb.net/?retryWrites=true&w=majority")

    # default caption 
    DEF_CAP = os.environ.get("DEF_CAP", "<b><a href='https//:t.me/Rkn_Botz'>{file_name} Main Telegram Channel: @RknDeveloper</a></b>",
    )

    # sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "CAACAgIAAxkBAAELFqBllhB70i13m-woXeIWDXU6BD2j7wAC9gcAAkb7rAR7xdjVOS5ziTQE")

    # admin id  ( required.. 😥)
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '893383574').split()]
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
