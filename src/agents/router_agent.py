
from .diet_agent import DietAgent
from .exercise_agent import ExerciseAgent
from .safety_agent import SafetyAgent
from .diet_agent import DietAgent

def route_query(q):
    q=q.lower()
    if "food" in q or "eat" in q: return DietAgent()
    if "exercise" in q or "walk" in q: return ExerciseAgent()
    if "drug" in q or "medicine" in q: return SafetyAgent()
    return DietAgent()
