import telebot
from google import genai

# আপনার টেলিগ্রাম বট টোকেন এবং জেমিনি এপিআই কী
BOT_TOKEN = "9058378811:AAEZzfh5jU5Ujz2fiB7I1H2yFstDIJgtxMM"
GEMINI_API_KEY = "AQ.Ab8RN6IjLgf0OWRUOJXEsdFGFBJgwLRtb_bGJ9vjNuhJSJXfnw"

# বট এবং জেমিনি ক্লায়েন্ট ইনিশিয়ালাইজ করা
bot = telebot.TeleBot(BOT_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(func=lambda message: True)
def reply_with_ai(message):
    try:
        # টেলিগ্রামে ইউজারকে 'typing...' স্ট্যাটাস দেখাবে যাতে মনে হয় বট ভাবছে
        bot.send_chat_action(message.chat.id, 'typing')
        
        # জেমিনি এআই মডেলকে কল করে উত্তর জেনারেট করা
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"তুমি একজন বুদ্ধিমান সহকারী। নিচের প্রশ্ন বা সমস্যাটি ভালোভাবে ভেবেচিন্তে সহজ, সুন্দর ও বিস্তারিত বাংলায় উত্তর দাও:\n\n{message.text}"
        )
        
        # ইউজারের মেসেজের জবাবে উত্তর পাঠানো
        bot.reply_to(message, response.text)
        
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "দুঃখিত, উত্তর তৈরি করতে একটু সমস্যা হয়েছে। আবার চেষ্টা করুন।")

print("বট সফলভাবে চালু হয়েছে এবং মেসেজের জন্য অপেক্ষা করছে...")
bot.infinity_polling()
