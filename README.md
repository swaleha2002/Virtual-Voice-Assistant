Sara - Virtual Assistant

## Project Overview
Sara is a virtual assistant built in Python designed to perform various tasks through voice commands. It integrates several APIs and local services to interact with the user, including performing web searches, sending emails, opening applications, checking weather, scheduling meetings, and much more.

## Features
- Voice Interaction: Uses `pyttsx3` for text-to-speech and `speech_recognition` for speech-to-text.
- Web Operations: Opens websites, plays videos, and fetches news using `webbrowser` and `requests`.
- Email Support: Sends emails through Gmail using `smtplib`.
- Weather Forecast: Fetches real-time weather data via OpenWeatherMap API.
- Jokes & Fun: Delivers jokes using `pyjokes`.
- Math Calculations: Performs calculations using the WolframAlpha API.
- System Operations: Can shut down or restart the computer.
- Schedule Management: Sets alarms and schedules meetings using `schedule`.
- Battery Check: Reports the system's battery percentage using `psutil`.

## Tech Stack
- Programming Language: Python 3.x
- Libraries: `pyttsx3`, `speech_recognition`, `wikipedia`, `webbrowser`, `os`, `smtplib`, `pyjokes`, `wolframalpha`, `requests`, `json`, `psutil`, `schedule`

## How to Run
1. Install Dependencies:
   Install the required libraries using pip:
   ```bash
   pip install pyttsx3 speechrecognition wikipedia pyjokes wolframalpha requests psutil schedule
   ```

2. Replace API Key:
   - Update the weather API key in `weather()` function.
   - Set your WolframAlpha API key for calculations.
   - Provide your Gmail credentials for the email feature.

3. Run the Program:
   Execute the script:
   ```bash
   python virtual_assistant.py
   ```

## Contributions
- Integrated voice recognition and speech output to provide an interactive user experience.
- Built a modular assistant with a wide range of functions such as email sending, weather checking, and scheduled tasks.
- Ensured easy customization with user-specific details like email credentials and API keys.

## License
This project is licensed under the MIT License.


This README briefly outlines the project, its features, tech stack, and usage. Adjust the details like API keys and paths as needed.
