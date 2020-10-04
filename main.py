from telegram.ext import Updater, CommandHandler
from mcstatus import MinecraftServer
from config import TG_TOKEN

servers = {}


def status(update, context):
    chat_id = update.message.chat_id
    if chat_id not in servers.keys():
        update.message.reply_text("Set server address with /server [ip] [port]")
        return

    server = servers[chat_id]

    try:
        status = server.status()
    except Exception:
        update.message.reply_text("Invalid server.")
        return

    if status.players.online != 0:
        players = [i.name for i in status.players.sample]
    else:
        players = []

    text =  f"Server online. Latency: {status.latency}.\n" \
            f"Players online: {', '.join(players)}"

    update.message.reply_text(text)


def setserver(update, context):
    try:
        chat_id = update.message.chat_id

        if len(context.args) not in [1,2]:
            raise Exception("Enter valid ip and port. Example: /setserver 192.168.0.1 25565")

        if len(context.args) == 1:
            server = MinecraftServer.lookup(context.args[0])
        else:
            server = MinecraftServer.lookup(f"{context.args[0]}:{context.args[1]}")

        servers[chat_id] = server

    except Exception as e:
        update.message.reply_text(str(e))

updater = Updater(TG_TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('mc', status))
updater.dispatcher.add_handler(CommandHandler('server', setserver))


updater.start_polling()
updater.idle()
