import telebot
from google import genai

# আপনার টেলিগ্রাম বট টোকেন এবং জেমিনি এপিআই কি
BOT_TOKEN = "9058378811:AAEZzfh5jU5Ujz2fiB7I1H2yFstDIJgtxMM"
GEMINI_API_KEY = "AQ.Ab8RN6Jion_4ChkftifEsBpOlu6AED5oQpO9paRH-pNtqZdkAQ"

# বট এবং জেমিনি ক্লায়েন্ট ইনিশিয়ালাইজ করা
bot = telebot.TeleBot(BOT_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(func=lambda message: True)
def reply_with_ai(message):
    try:
        # টেলিগ্রামে ইউজারের জন্য 'typing...' স্ট্যাটাস দেখানো
        bot.send_chat_action(message.chat.id, 'typing')
        
        # ইউজারের মেসেজটি জেমিনি এআই মডেলে পাঠানো
        user_message = message.text
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"তুমি একজন বুদ্ধিমান সহায়ক এআই। ইউজারের প্রশ্নের উত্তর দাও: {user_message}"
        )
        
        # ইউজারের মেসেজের জবাবে উত্তর পাঠানো
        bot.reply_to(message, response.text)
        
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "দুঃখিত, এই মুহূর্তে উত্তর দিতে সমস্যা হচ্ছে। একটু পরে আবার চেষ্টা করুন।")

print("বট সফলভাবে চালু হয়েছে এবং মেসেজ শোনার জন্য প্রস্তুত...")
bot.infinity_polling()
