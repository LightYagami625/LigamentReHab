#  LigamentReHab – Voice-Guided Rehab Exercise Assistant

LigamentReHab is a voice-assisted Python application designed to help you through a guided routine of physiotherapy exercises — especially helpful for knee ligament injury recovery. The program uses text-to-speech to guide you step-by-step through each exercise in real-time.


🚀 **Features**
- 🔊 Voice prompts for every exercise using pyttsx3

- ⏱️ Automatic timed laps and counts

- 🧠 Easy-to-use modular structure (app.py is the main controller)

- 🛌 Exercises include pillow squeezes, leg raises, knee bends, hip movements, and more


**Structure of the Program**
<pre>LigamentReHab/
├── app.py         # Main execution file – run this to start the exercises
├── main.py        # Contains core logic for counting and laps
└── README.md      # Project documentation
</pre>

🧑‍💻 **How to Run**
1. ✅ Install Required Library
The app uses only one external Python library:
<pre> ### 📦 Install Required Library ```bash pip install pyttsx3 ``` </pre>
Note: pyttsx3 works offline and uses your system's TTS engine.


2. ▶️ Run the Program
To start the exercise routine, simply run:
<pre> ### 📦 Install Required Library ```bash python app.py ``` </pre>
Each exercise will be announced, counted, and timed automatically with breaks in between.

###🧘 **Exercises Included**
  1. Knee Exercise
  2. Pillow Press Exercise
  3. Strengthening Exercise
  4. Leg Folding
  5. Leg Bending Sidewise
  6. Hip Upward Movement
  7. Hip Sidewise Movement
  8. Hip Downward Movement
  

📌 **Notes**
Make sure your speakers are on or headphones connected — the guidance is through voice.

Modify the lap counts and durations in main.py if your rehab plan needs adjustment.

💪 Contribution
This project was made for personal rehab needs. Feel free to fork it and adapt it for your physiotherapy use cases!

