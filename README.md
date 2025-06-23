# 🎓 CourseCrafter

**CourseCrafter** is an intelligent multi-agent system that auto-generates bite-sized courses from a single topic — complete with a course structure, PowerPoint slides, and a quiz in Word format. Powered by the Google Agent Development Kit (ADK) and Gemini models.

---

## 🚀 Features

-  Auto-generates structured course modules from a topic  
-  Quiz generator – Outputs `.docx` file using `python-docx`  
-  Slide designer – Creates dynamic `.pptx` presentations  
-  Multi-agent orchestration using Google ADK

---

## ⚙️ Tech Stack

- Google ADK (Agent Development Kit)
- python-docx – Quiz document creation
- python-pptx – PowerPoint slide generation
- Python 3.11+

---

## Testing Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/janisrebekah/CourseCrafter.git
   cd CourseCrafter
   
2. **Set up virtual environment**

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install dependencies**

pip install -r requirements.txt

4. **Run the ADK web app**
   
adk web

5. **Open your browser**
Navigate to http://localhost:8000

Enter a course topic (e.g., Artificial Intelligence)

**The agent will generate:**\
1. A course module (JSON)\
2. A quiz in .docx\
3. A presentation in .pptx\
4. All files will be saved in the project directory


