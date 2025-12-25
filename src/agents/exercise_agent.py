
import google.generativeai as genai, os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
m=genai.GenerativeModel("gemini-1.5-flash")
class ExerciseAgent:
    def run(self,q,c):
        return m.generate_content(f"Exercise advice. {c} {q}").text
