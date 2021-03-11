from Luna import CMD_HELP
import os
import urllib.request
from typing import List
from typing import Optional
from requests import get
from telethon import *
from telethon.tl import functions
from telethon.tl import types
from telethon.tl.types import *

from Luna import *


@register(pattern="^/git")
async def _(event):
    if event.fwd_from:
        return
    
    text = event.text[len("/git ") :]
    usr = get(f"https://api.github.com/users/{text}").json()
    if usr.get("login"):
        reply_text = f"""**Name:** `{usr['name']}`
**Username:** `{usr['login']}`
**Account ID:** `{usr['id']}`
**Account type:** `{usr['type']}`
**Location:** `{usr['location']}`
**Bio:** `{usr['bio']}`
**Followers:** `{usr['followers']}`
**Following:** `{usr['following']}`
**Hireable:** `{usr['hireable']}`
**Public Repos:** `{usr['public_repos']}`
**Public Gists:** `{usr['public_gists']}`
**Email:** `{usr['email']}`
**Company:** `{usr['company']}`
**Website:** `{usr['blog']}`
**Last updated:** `{usr['updated_at']}`
**Account created at:** `{usr['created_at']}`
"""
    else:
        reply_text = "User not found. Make sure you entered valid username!"
    await event.reply(reply_text)


@register(pattern="^/repo (.*)")
async def _(event):
    if event.fwd_from:
        return
    
    text = event.pattern_match.group(1)
    usr = get(f"https://api.github.com/users/{text}/repos?per_page=300").json()
    reply_text = "**Repo**\n"
    for i in range(len(usr)):
        reply_text += f"[{usr[i]['name']}]({usr[i]['html_url']})\n"
    await event.reply(reply_text, link_preview=False)


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /git <username>: Returns info about a GitHub user or organization.
 - /repo <username>: Return the GitHub user or organization repository list
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
