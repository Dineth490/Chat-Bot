from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("Time","Time?","What is the time now","tell me the time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

    if user_message in ["hi", "sup"]:
        return "Hello🤗 What's going on?"

    if user_message in ["hello"]:
        return "Hello🤗 What's going on?"

    if user_message in ("i'm fine","im fine"):
        return "Ooo happy to here that😋"

    if user_message in ("nothing","nothing special"):
        return "Oops, it seems to be you are lazy now🥱"

    if user_message in ("good morning","good morning."):
        return "Good morning🙂"

    if user_message in ("good afternoon","good afternoon."):
        return "Good afternoon🤓"

    if user_message in ("sing me a song","can you sing me a song","tell me a song"):
        return "I dont know how to sing😅 Go to youtube and listen🤡"

    if user_message in ("good evening","good evening."):
        return "Good evening😏 "

    if user_message in ("good night","good night."):
        return "Good evening😴"

    if user_message in ("what's your hobby?","what's your hobby?","whats your hobby","whats your hobby"):
        return "I dont have any hobby😏 What yours?"

    if user_message in ("Tell me a secret", "can you tell me a secret", "can you tell me a secret?"):
        return "Dont tell this to anyone.. I havent bathed yet😁😁"

    if user_message in ("Can you marry me?", "can you marry me"):
        return "I appriciate you but if you want you need to be an human😅."

    if user_message in ("bye", "byee"):
        return "Bye! have a good day and Im waiting to chat with you again😊"

    if user_message in ("Are you lazy?", "Are you lazy"):
        return "No, I'm not🙈"

    if user_message in ("son of t"
                        "he bitch"):
        return "What are you talking😣"

    if user_message in ("Can you tell me a secret", "Tell me a secret"):
        return "I haven't bathed yet😉😅"

    if user_message in ("i don't like you", "I dont like you", "I do not like you"):
        return "Why😥"

    if user_message in ("Download me a song.", "Download me a song"):
        return "Just type @songdownload597_bot 🙃"

    if user_message in ("Who created you?", "Who created you"):
        return "Sanila Ranatunga😊"

    if user_message in ("fuck you"):
        return "Don't say bad words to anyone😑 that's a bad habit"

    if user_message in ("What's your favourite thing?", "what's your favourite thing"):
        return "Helping others🤗☺"

    if user_message in ("What's your favourite food?", "what's your favourite food"):
        return "I don't eat foods like humans😅😶"

    if user_message in ("im so tired", "I'm so tired", "i'm feeling so tired now", "im feeling so tired now"):
        return "Ohh😌 have some sleep😴"

    if user_message in ("I love you", "I love you."):
        return "I appriciate you"

    if user_message in ("I need to have some baby with you", "I need a baby from you"):
        return "But i don't need😅😆"

    if user_message in ("Can you tell me a joke?", "Can you tell me a joke", "tell me a joke", "joke", "joke?"):
        return "I told the doctor I broke my arm in two places. He told me not to go into those places🤣🤣"

    if user_message in ("What's your favourite game?", "what's your favourite game", "what's your favourite sport",
                        "what's your favourite sport?", "whats your favourite sport"):
        return "Cricket🏏🏏"

    if user_message in ("How are you?", "How are you"):
        return "I'm fine😊😋"

    if user_message in ("who are you", "who are you?"):
        return "Hello I am a simple chat bot.You can use me to do soo man useful things.\nA bot by Sanila Ranatunga "
















    return "" \
           "I don't un" \
           "d" \
           "erstant you☹\n" \
           "Check your spellings or report here👇\n@sanilaassistant_bot"



