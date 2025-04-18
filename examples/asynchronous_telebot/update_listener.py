from blebot.async_blebot import Asyncblebot

# Update listeners are functions that are called when any update is received.

bot = Asyncblebot(token='TOKEN')

async def update_listener(messages):
    for message in messages:
        if message.text == '/start':
            await bot.send_message(message.chat.id, 'Hello!')

bot.set_update_listener(update_listener)


import asyncio
asyncio.run(bot.polling())