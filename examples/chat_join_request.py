import blebot


bot = blebot.blebot('TOKEN')

@bot.chat_join_request_handler()
def make_some(message: blebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

bot.infinity_polling(allowed_updates=blebot.util.update_types)