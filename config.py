import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    startmsg = (
        'ʙᴏᴛ sᴜᴅᴀʜ ᴀᴋᴛɪғ ᴅᴀɴ ʙᴇʀᴊᴀʟᴀɴ. ʙᴏᴛ ɪɴɪ '
        'ᴅᴀᴘᴀᴛ ᴍᴇɴʏɪᴍᴘᴀɴ ᴘᴇsᴀɴ ᴅᴀʟᴀᴍ ᴏʙʀᴏʟᴀɴ ᴋʜᴜsᴜs, '
        'ᴅᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴍᴇɴɢᴀᴋsᴇsɴʏᴀ ᴍᴇʟᴀʟᴜɪ ʙᴏᴛ.'
    )
    forcemsg = (
        'ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪʙᴀɢɪᴋᴀɴ ᴏʟᴇʜ ʙᴏᴛ. '
        'ɢᴀʙᴜɴɢ ᴅᴜʟᴜ, ʟᴀʟᴜ ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ᴄᴏʙᴀ ʟᴀɢɪ.'
    )

    API_ID = int(os.environ.get('API_ID', 27538621))
    API_HASH = os.environ.get('API_HASH', '24c338d23154f5ea8adb9fc684a4a06f')
    OWNER_ID = int(os.environ.get('OWNER_ID', 487936750))
    MONGO_URL = os.environ.get('MONGO_URL', 'mongodb://root:passwd@mongo')

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
    DATABASE_ID = int(os.environ.get('DATABASE_ID', '-1002386387886'))

    BOT_ID = BOT_TOKEN.split(':', 1)[0]


Config = Config()
