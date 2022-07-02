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
    fallen = await message.reply("» Processing query...")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await YashuAlpha.get_me()
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
                        "<b>» Invite members right required to invite music assistant !</b>")
                    return

                try:
                    await YashuAlpha.join_chat(invitelink)
                    await YashuAlpha.send_message(
                        m.chat.id, "» Assistant joined !")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await fallen.edit(
                        f"<b>» Music player assistant not in this chat, Try: /join")
    try:
        await YashuAlpha.get_chat(chid)
    except Exception as e:
        await fallen.edit(
            f"<i>» Failed to join !</i>\n\Cause : {e}")
        return

    if replied:
        if replied.audio or replied.voice:
            omfoo = await replied.reply("**__fetching audio__** 🎧 ")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:70]
                else:
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:70]
                    else:
                        songname = "Audio"
                dur = replied.audio.duration
            elif replied.voice:
                songname = "Voice note"
                dur = replied.voice.duration

    elif len(m.command) == 2:
        query = m.text.split(None, 1)[1]
        omfoo = await m.reply("**__Searching query__**")
        
            
