OWNER_ID = 1221693726
from Luna import tbot
from Luna.events import register
from Luna.modules.sql.mute_sql import is_muted, mute, unmute
from telethon import events
import asyncio
from telethon.tl.functions.users import GetFullUserRequest

@register(pattern="^/gmute ?(.*)")
async def gmute(event):
    if event.sender_id == OWNER_ID:
       pass
    else:
      return
    reply = await event.get_reply_message()
    userid = reply.sender_id
    if is_muted(userid, "gmute"):
        return await event.reply("This user is already gmuted")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.reply("Error occured!\nError is " + str(e))
    else:
        await event.reply("Successfully gmuted that person")

@register(pattern="^/ungmute ?(.*)")
async def ungmute(event):
    if event.sender_id == OWNER_ID:
       pass
    else:
      return
    reply = await event.get_reply_message()
    userid = reply.sender_id
    if not is_muted(userid, "gmute"):
        return await event.reply("This user is not gmuted")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.reply("Error occured!\nError is " + str(e))
    else:
        await event.reply("Successfully ungmuted that person")


@tbot.on(events.NewMessage(pattern=None))
async def lel(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()

