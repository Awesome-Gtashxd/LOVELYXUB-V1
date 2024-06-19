import pyrogram
import strings
import config

from Lovely import bot, lovely
from Lovely.helpers.helper_funcs import get_datetime 

async def run_clients():
      await bot.start()
      await lovely.start()
      await pyrogram.idle()
      zone = await get_datetime()
      await bot.send_message(
           chat_id=config.SUPPORT_CHAT,
           text=strings.RESTART_TEXT1.format(date=zone["date"], time=zone["time"]))
      await lovely.send_message(
           chat_id=config.SUPPORT_CHAT,
           text=strings.RESTART_TEXT2.format(date=zone["date"], time=zone["time"]))

if __name__ == "__main__":
    lovely.loop.run_until_complete(run_clients())
