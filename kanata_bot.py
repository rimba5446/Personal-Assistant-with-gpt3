import openai
import speech_recognition as sr
import pyttsx3
import yaml

config = yaml.safe_load(open("config.yml"))
openai.api_key = config["GPT_API"]

def chatbot(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=2,
        stop=None,
        temperature=1.5,
    )

    message = completions.choices[0].text
    return message

def get_audio_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your Voice:")
        audio = r.listen(source)

    try:
        text = r.recognize_sphinx(audio)
        print("You said: {}".format(text))
        return text
    except:
        print("Sorry, I didn't get that.")
        return None

def play_audio_output(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    print (rate)
    engine.setProperty('rate', 165)
    volume = engine.getProperty('volume')
    print (volume)
    engine.setProperty('volume',2.0)
    voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[0].id) #male voices
    engine.setProperty('voice', voices[1].id) #female voices
    engine.say(text)
    engine.runAndWait()


kanata_history = []
print("Hi, I am Kanata, your personal voice assistant. How can I help you today?🤗")
play_audio_output("Hi, I am Kanata, your personal voice assistant. How can I help you today?🤗")

while True:
    user_input = get_audio_input()
    if user_input is None:
        print("Sorry, I didn't get that.")
        play_audio_output("Sorry, I didn't get that.")
        continue
    if "bye" in user_input.lower():
        print("Goodbye! Have a great day.")
        play_audio_output("Goodbye! Have a great day.")
        break
    kanata_history.append("You: " + user_input)
    prompt = "\n".join(kanata_history)
    response = chatbot("Kanata: " + prompt)
    print("Kanata: " + response)
    play_audio_output(response)
    kanata_history.append(response)

