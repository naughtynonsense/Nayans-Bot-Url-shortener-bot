import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '4011894'))
API_HASH = environ.get('API_HASH', '56ac06547b5d8af50493e104feed8053')
BOT_TOKEN = environ.get('BOT_TOKEN', "5846833594:AAGF5qK1HlD1JlqeCm8aco9SpoP7d98D8Ag")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/e4afc768df4d8164f0085.jpg https://telegra.ph/file/59b914674624cec669c10.jpg https://telegra.ph/file/3dc0011ea640724a3e5ea.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '739667270').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '739667270').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001565856771')
auth_grp = environ.get('AUTH_GROUP', '-1001694316223')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://NAYANS:NAYANS@cluster0.hy39lmc.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001555083458'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'SixFlix')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b><i>ᴛɪᴛʟᴇ:</b></i> <code>{file_name}</code>\n▬▬▬▬▬▬▬▬▬▬▬▬\n🍃<b><i>Movies Update Channel</b></i>🍃\n<i>https://t.me/+ERyRrnI5CPEyYmFl</i>\n🍃<b><i>Series Update Channel</b></i>🍃\n<i>https://t.me/+4NvHgqi9_FRhNjY1</i>\n▬▬▬▬▬▬▬▬▬▬▬▬\n☘𝙅𝙤𝙞𝙣:-<b><i>https://t.me/freakersfilmy</b></i>\n\n🧐𝙁𝙧𝙚𝙖𝙠𝙚𝙧𝙨🎭𝙁𝙞𝙡𝙢𝙮™🍿©\n100% ғᴀꜱᴛ & ϙᴜᴀʟɪᴛʏ\n▬▬▬▬▬▬▬▬▬▬▬▬")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION",)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<i><b>ᴛɪᴛʟᴇ</i></b>: <b><a href={url}>{title}</a> [{year}]</b>\n<i><b>ᴅᴜʀᴀᴛɪᴏɴ</i></b>:<i> {runtime} Mins</i>\n<i><b>ᴀʟsᴏ ᴋɴᴏᴡ ᴀs</i></b>:<i> {title}</i>\n<i><b>ʀᴀᴛɪɴɢ</i></b>: <b><a href={url}>IMDb</a></b>⭐️ <i>{rating}/10</i>\n<i><b>ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ</i></b>: <i>{release_date}</i> \n<i><b>ɢᴇɴʀᴇ</i></b> :<i> <a href={url}>{genres}</a></i> \n<i><b>ʟᴀɴɢᴜᴀɢᴇ</i></b>: <i>{languages}</i>\n<i><b>ᴄᴏᴜɴᴛʀʏ ᴏғ ᴏʀɪɢɪɴ</i></b>: <i>#{countries}</i>\n\n<i><b>sᴛᴏʀʏ ʟɪɴᴇ</i></b>: <i>{plot}</i>\n\n<i><b>ᴅɪʀᴇᴄᴛᴏʀs</i></b>: <i><a href={url}>{director}</a></i>\n<i><b>ᴡʀɪᴛᴇʀs </i></b>: <i><a href={url}>{writer}</a></i> \n\n<i><b>ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ</i></b> : <i>[ғʀᴇᴀᴋᴇʀsғɪʟᴍʏ](https://t.me/freakersfilmy)</i>\n☘𝙅𝙤𝙞𝙣: <i>https://t.me/freakersmovie</i>\n\n🧐𝙁𝙧𝙚𝙖𝙠𝙚𝙧𝙨🎭𝙁𝙞𝙡𝙢𝙮🍿\n  100% 𝑭𝒂𝒔𝒕 & 𝑸𝒖𝒂𝒍𝒊𝒕𝒚\n▬▬▬▬▬▬▬▬▬▬▬▬\n")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "True"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001855090915 -1001661137244')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##
    
      # URL Shortener #

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'atglinks.com')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '2948014f60b7700cbc5bca4a6b241b31f1ccd39c')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 3600))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "🤔𝙃𝙤𝙬 𝙏𝙤 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙❓"
DOWNLOAD_TEXT_URL = "https://t.me/SixFlix/308"

   # Custom Caption Under Button #
CAPTION_BUTTON = "sᴜʙsᴄʀɪʙᴇ"
CAPTION_BUTTON_URL = "https://t.me/freakers_series"

   # Auto Delete For Bot Sending Files #
