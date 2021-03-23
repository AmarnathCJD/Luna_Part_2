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
    if event.sender_id:
       pass
    else:
       return
    private = False
    if event.fwd_from:
        return
    if event.is_private:
        await event.reply("Unexpected issues or ugly errors may occur!")
        private = True
    reply = await event.get_reply_message()

    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.reply("Please reply to a user or add their username into the command to ungmute them.")
    replied_user = await event.client(GetFullUserRequest(userid))
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

