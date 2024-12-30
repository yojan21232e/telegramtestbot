import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# (Opcional) Configura el logging para ver mensajes de depuración
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /start y devuelve tu chat ID."""
    chat_id = update.effective_chat.id
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"¡Hola! Tu chat ID es: {chat_id}"
    )

def main():
    # Reemplaza 'TU_TOKEN_AQUI' con el token de tu bot
    application = ApplicationBuilder().token("7819209412:AAFAVtYwh3ejFORoAqVx-HArF9G6Gg-FIMY").build()

    # Agregamos un handler para /start
    application.add_handler(CommandHandler("start", start))

    # Iniciamos la lectura de mensajes
    application.run_polling()

if __name__ == "__main__":
    main()
