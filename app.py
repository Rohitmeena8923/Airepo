from flask import Flask, request, send_file
from plugins.master import download_content
import threading
from telegram.ext import Updater, CommandHandler
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        platform = request.form['platform']
        try:
            file_path = download_content(url, platform)
            return send_file(file_path, as_attachment=True)
        except Exception as e:
            return f"<h3>Error: {str(e)}</h3>", 400
    return '''
        <h1>TXT-Master-All (Render Edition)</h1>
        <form method="post">
            URL: <input name="url" type="text"><br>
            Platform: <input name="platform" type="text"><br>
            <input type="submit" value="Download">
        </form>
    '''

def start_bot():
    TOKEN = os.environ.get('BOT_TOKEN')
    if not TOKEN:
        print("BOT_TOKEN not set in environment variables.")
        return
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    def start(update, context):
        update.message.reply_text('🤖 Hello! The TXT-Master bot is running.')

    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    # Start the bot in a separate thread
    threading.Thread(target=start_bot, daemon=True).start()
    # Run Flask app
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
