import re
import json
import random
import datetime

class RuleBasedAgent:
    """Simple rule-based agent class."""

    def __init__(self, intents_path = "intents.json", log_path = "chat_log.txt"):
        # Loading intents from JSON
        with open(intents_path, "r", encoding="utf-8") as f:
            self.intents = json.load(f)

        self.log_path = log_path
        # Create LOg file
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(f"\n--- New session: {datetime.datetime.now()} ---\n")

    def preprocess(self, text):
        """Text cleaning: removing lowercase letters and symbols"""
        text = text.lower()
        text = re.sub(r"[^a-zа-яё0-9\s\u0400-\u04FF]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text
    
    def predict_intent(self, text):
        """Text-based intent detection."""
        text = self.preprocess(text)
        for intent, data in self.intents.items():
            for patt in data["patterns"]:
                if re.search(patt, text):
                    return intent
        return "unknown"
    
    def get_response(self, text):
        """Responding to an Intent"""
        intent = self.predict_intent(text)
        response = random.choice(self.intents[intent]["responses"])
        # Let's write a log.
        self.log_interaction(text, response)
        return response
    
    def log_interaction(self, user_text, agent_response):
        """Save conversation history to a file."""
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(f"Siz: {user_text}\nAgent: {agent_response}\n")

def main():
    agent = RuleBasedAgent(intents_path="intents.json")
    print("Oddiy AI agent ishga tushdi! (chiqish uchun 'exit' yoki 'xayr' yozing).")
    while True:
        user = input("Siz: ").strip()
        if not user:
            continue
        response = agent.get_response(user)
        print("Agent:", response)
        if agent.predict_intent(user) == "xayr":
            break

if __name__ == "__main__":
    main()

