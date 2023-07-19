#import all packages before running this code
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import wolframalpha
import requests
import json
import psutil
import schedule

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Sara, your virtual assistant. How can I assist you today?")


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return "None"

    return query


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender_email@gmail.com', 'your_password')  # Replace with your email credentials
    server.sendmail('reciever_email@gmail.com', to, content)
    server.close()


def open_wikipedia(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)


def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        if current_time == alarm_time:
            speak("Wake up!")
            break


def set_meeting(meeting_time):
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    if current_time == meeting_time:
        speak("Meeting time")
        # Perform any additional actions for the scheduled meeting


if __name__ == '__main__':
    wish_me()
    while True:
        query = take_command().lower()

        if 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'play' in query and 'youtube' in query:
            query = query.replace("play", "")
            query = query.replace("youtube", "")
            speak(f"Playing {query} on YouTube")
            webbrowser.open(f"youtube.com/results?search_query={query}")

        elif 'weather' in query:
            api_key = "API"  # Replace with your OpenWeatherMap API key
            base_url = "https://api.openweathermap.org/data/2.5/weather?q=India,in&appid={API}"
            speak("What's the city name?")
            city_name = take_command().lower()
            complete_url = base_url + "&appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            data = response.json()
            if "cod" in data and data["cod"] != "404":
                if "main" in data:
                    main_data = data["main"]
                    temperature = main_data.get("temp")
                    humidity = main_data.get("humidity")
                    weather_data = data.get("weather")
                    if temperature is not None and humidity is not None and weather_data is not None and len(
                            weather_data) > 0:
                        weather_description = weather_data[0].get("description")
                        if weather_description is not None:
                            speak(
                                f"The temperature in {city_name} is {temperature} Kelvin with {weather_description} and {humidity}% humidity.")
                        else:
                            speak("Sorry, I couldn't fetch the weather information.")
                    else:
                        speak("Sorry, I couldn't fetch the weather information.")
                else:
                    speak("Sorry, I couldn't fetch the weather information.")
            else:
                speak("Sorry, I couldn't fetch the weather information.")



        elif 'date' in query:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"The current date is {date}")

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time}")

        elif 'day' in query:
            day = datetime.datetime.now().strftime("%A")
            speak(f"Today is {day}")

        elif 'shutdown' in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 1")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = take_command()
                speak("Whom should I send it to?")
                to = input("Recipient's email: ")  # You can use voice command to get recipient's email as well
                send_email(to, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(str(e))
                speak("Sorry, I couldn't send the email. Please try again.")

        elif 'open powerpoint' in query:
            ppt_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"  # Replace with the path to your PowerPoint presentation
            os.startfile(ppt_path)
            speak("Opening PowerPoint presentation")

        elif 'open visual studio code' in query:
            code_path = "C:\\Users\\vscode\\OneDrive\\Desktop\\Visual Studio Code.lnk" # Replace with the path to your Visual Studio Code executable
            os.startfile(code_path)
            speak("Opening Visual Studio Code")

        elif 'write code' in query:
            speak("Sure! What code should I write?")
            code = take_command()
            with open("code.py", "w") as file:
                file.write(code)
            speak("Code written successfully!")

        elif 'update assistant' in query:
            # Place your assistant update code here
            speak("Assistant updated successfully!")

        elif 'battery' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"The current battery level is {percentage} percent")

        elif 'news' in query:
            try:
                jsonObj = requests.get(
                    "https://newsapi.org/v2/everything?q=tesla&from=2023-06-07&sortBy=publishedAt&apiKey=new_api"  # Replace with your NewsAPI API key
                )
                data = json.loads(jsonObj.text)
                speak("Here are some top news headlines from the Times of India")
                for i, item in enumerate(data["articles"]):
                    if i < 5:  # Speak only the top 5 headlines
                        speak(item['title'])
            except Exception as e:
                print(str(e))
                speak("Sorry, I couldn't fetch the news. Please try again.")

        elif 'open website' in query:
            speak("Which website would you like me to open?")
            website = take_command().lower()
            webbrowser.open(website)

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'calculate' in query:
            speak("Sure! What do you want to calculate?")
            question = take_command()
            app_id = "your_api"  # Replace with your WolframAlpha app ID
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(f"The answer is {answer}")

        elif 'set alarm' in query:
            speak("Sure! What time should I set the alarm for?")
            alarm_time = take_command()
            set_alarm(alarm_time)

        elif 'schedule meeting' in query:
            speak("Sure! What time should I schedule the meeting for?")
            meeting_time = take_command()
            schedule.every().day.at(meeting_time).do(set_meeting, meeting_time)

        elif 'exit' in query:
            speak("Goodbye!")
            exit()

        else:
            speak("Sorry, I didn't understand that. Can you please repeat?")