
import google.generativeai as genai, os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
m=genai.GenerativeModel("gemini-1.5-flash")
class DietAgent:
    def run(self,q,c):
        return m.generate_content(f"Diet advice. {c} {q}").text
