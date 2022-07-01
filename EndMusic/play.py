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
    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Anonymous"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await fallen.edit(
                        "<b>» Admin rights required !</b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "» Assistant joined !")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await fallen.edit(
                        f"<b>» Music player assistant not in this chat, Try: /join")
    try:
        await USER.get_chat(chid)
    except Exception as e:
        await fallen.edit(
            f"<i>» Failed to join !</i>\n\Cause : {e}")
        return
