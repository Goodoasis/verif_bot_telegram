from random import randint

from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from api_verif.api_verif import ApiVerif
from interface.to_telegram import ToTelegram


TOKEN = '2136748322:AAGFFJAJagU16Bhm7Qf-F0d-5N27HFqsnwk'


def start(update, context):
    update.message.reply_text("""
Bienvenue sur le bot de vérifs.

Les commandes disponibles sont :
- Entrer un nombre entre 0 et 99 pour recevoir la vérifications du permis correspondante.
- Entrer '!' pour obtenir une vérif aléatoire.
- /help pour avoir de l'aide.
- /credit pour savoir qui se cache derriere.
    """)

def credit(update, context):
    update.message.reply_text("Made by GoodOasis")

def help(update, context):
    update.message.reply_text("""Les commandes disponibles sont :
- Envoyer un nombre entre 0 et 99 pour recevoir la vérifications du permis.
- '!' pour obtenir une vérif aléatoire.
- /Credit pour savoir eltui se cache derriere""")

def message_text(update, context):
    """Analyse le message pour repondre."""
    msg_text = update.message.text
    if msg_text.isdigit():  # Si seulement des chiffres.
        ask_answer = ApiVerif.get_verif(int(msg_text))
        formated_answer = ToTelegram.compose_messages(ask_answer)

    elif msg_text == "!":   # Random si l'user a envoyé "!".
        ask_answer = ApiVerif.get_verif(randint(0, 99))
        formated_answer = ToTelegram.compose_messages(ask_answer)

    else:                   # Si la demande n'est pas correcte.
        formated_answer = ["Demande incorrecte."]
    # On envoie les messages:
    for msg in formated_answer:
        update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)


def main():
    # La classe Updater permet de lire en continu le channel.
    updater = Updater(TOKEN, use_context=True)
    # Pour avoir accès au dispatcher plus facilement.
    dp = updater.dispatcher
    # On ajoute des gestionnaires de commandes.
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("credit", credit))
    dp.add_handler(CommandHandler("help", help))
    # Pour gérer les messages texte.
    dp.add_handler(MessageHandler(Filters.text, message_text))
    # Sert à lancer le bot.
    updater.start_polling()
    # Pour arrêter le bot proprement.
    updater.idle()


if __name__ == '__main__':
    main()