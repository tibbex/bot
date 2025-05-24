from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace with your bot token from @BotFather
BOT_TOKEN = '7574955917:AAEVAjxFuNFP2bH52UakCdj8RSD5vQTAhs0'

# The subscription message
AI_SUBSCRIPTION_MESSAGE = """
🤖✨ AI Subscription Plans – Choose Your Power Level!

📅 Monthly Plans

🟢 Basic AI – Just the Basics  
💬 1,000 prompts/week  
🖼️ No image generation  
🌐 Simple Web UI  
🧠 1 AI Model  
💰 300 birr/month

🔵 Standard AI – Supercharged Smarts  
💬 100,000 prompts/week  
🖼️ No image generation  
🎨 Sleek Web UI  
🧠🧠🧠 3 AI Models  
💰 500 birr/month

🔴 Premium AI – Full Power Mode!  
♾️ Unlimited Prompts  
🖼️ Image Generation 🔥  
💻 Beautiful Web UI  
🧠🧠🧠🧠🧠 5 AI Models  
💰 800 birr/month

🕰️ 6-Month Plans (Best Value!)  
💥 Get 15% OFF on your first payment! 💸

🟢 Basic AI – Long Term Genius  
📈 1,000 prompts/day  
🖼️ No image generation  
🌐 Simple Web UI  
🧠 1 AI Model  
💳 3000 birr/6 months  
🎉 Only 2550 birr with first-time 15% discount!

🔵 Standard AI – Smart for Months  
📈 10,000 prompts/day  
🖼️ No image generation  
🎨 Sleek Web UI  
🧠🧠🧠 3 AI Models  
💳 6000 birr/6 months  
🎉 Only 5100 birr with first-time 15% discount!

🔴 Premium AI – Go Ultra  
♾️ Unlimited Prompts  
🖼️ Image Generation 🔥  
💻 Beautiful Web UI  
🧠🧠🧠🧠🧠 5 AI Models  
💳 9000 birr/6 months  
🎉 Only 7650 birr with first-time 15% discount!

📩 Contact / DM: https://t.me/aiassistdd
"""

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(AI_SUBSCRIPTION_MESSAGE)

# Main function to run the bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
