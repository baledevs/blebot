
import blebot
from blebot.async_blebot import Asyncblebot



bot = Asyncblebot('TOKEN')


@bot.message_handler(commands=['photo'])
async def photo_send(message: blebot.types.Message):
    with open('test.png', 'rb') as new_file:
        await bot.send_photo(message.chat.id, new_file)

@bot.message_handler(commands=['document'])
async def document_send(message: blebot.types.Message):
    with open('test.docx', 'rb') as new_file:
        await bot.send_document(message.chat.id, new_file)

@bot.message_handler(commands=['photos'])
async def photos_send(message: blebot.types.Message):
    with open('test.png', 'rb') as new_file, open('test2.png', 'rb') as new_file2:
        await bot.send_media_group(message.chat.id, [blebot.types.InputMediaPhoto(new_file), blebot.types.InputMediaPhoto(new_file2)])
    



import asyncio
asyncio.run(bot.polling())
