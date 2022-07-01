from . import *

@End.on_message(filters.command(["play", f"play@{BOT_USERNAME}"]) & filters.group & ~filters.bot & ~filters.edited & ~filters.forwarded)
async def play_func(_, m: MyHeartYashvi):
    user_id = m.from_user.id
    user_name = m.from_user.first_name
    replied = m.reply_to_message
    if m.sender_chat:
        return await m.reply("Looks like you're an anonymous, try without anonymous 🤧")
    if not user_id:
        return
    
