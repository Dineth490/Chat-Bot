from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","sup"):
        return "Hello! What's going on?🤔🙂"

    if user_message in ("Tell me a secret","can you tell me a secret","can you tell me a secret?"):
        return "Dont tell this to anyone.. I havent bathed yet😁😁"

    if user_message in ("Can you marry me?","can you marry me"):
        return "I appriciate you but if you want you need to be an human😅."

    if user_message in ("bye","byee"):
        return "Bye! have a good day and Im waiting to chat with you again😊"

    if user_message in ("What can you do?","What can you do"):
        return "I can tell you the local time (send me msg as time), and chat with you when you feel lazy🥱 and soo many things🙂🤗"

    if user_message in ("fuck you"):
        return "Don't say bad words to anyone😑 that's a bad habit"

    if user_message in ("What's your favourite thing?","what's your favourite thing"):
        return "Helping others🤗☺"

    if user_message in ("What's your favourite food?","what's your favourite food"):
        return "I don't eat foods like humans😅😶"

    if user_message in ("im so tired","I'm so tired","i'm feeling so tired now","im feeling so tired now"):
        return "Ohh😌 have some sleep😴"

    if user_message in ("I love you","I love you."):
        return "I appriciate you"

    if user_message in ("I need to have some baby with you","I need a baby from you"):
        return "But i don't need😅😆"

    if user_message in ("What do you do in your lazy time","What do you do in your lazy time?"):
        return "I haven't feel lazy like humans😉"

    if user_message in ("Can you tell me a song","Can you tell me a poem","Can you tell me a poem?","can you sing a "
                                                                                                    "song for me?"):
        return "Ummm🤕 I don't how to sing😞 sorry😪😌"

    if user_message in ("Can you tell me a joke?","Can you tell me a joke","tell me a joke","joke","joke?"):
        return "I told the doctor I broke my arm in two places. He told me not to go into those places🤣🤣"


    if user_message in ("What's your favourite game?","what's your favourite game","what's your favourite sport","what's your favourite sport?","whats your favourite sport"):
        return "Cricket🏏🏏"

    if user_message in ("How are you?","How are you"):
        return "I'm fine😊😋"

    if user_message in ("babbaaaaa"):












     if user_message in ("who are you","who are you?"):
        return "Hello I am a simple chat bot.You can use me to do soo man useful things.(A bot by @SanilaRanatunga)"
    if user_message in ("time","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I dont understand you☹☹ just send /help to know how to use me🙂"
