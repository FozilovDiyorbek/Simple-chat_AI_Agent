import re
import json
import random
import datetime

class RuleBasedAgent:
    """Oddiy qoidaga asoslangan agent klassi."""

    def __init__(self, intents_path = "intents.json", log_path = "chat_log.txt"):
        # Jsondan intents yuklash
        with open(intents_path, "r", encoding="utf-8") as f:
            self.intents = json.load(f)

        self.log_path = log_path
        # Log faylini yaratamiz
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(f"\n--- Yangi sessiya: {datetime.datetime.now()} ---\n")

    def preprocess(self, text):
        """Matn tozalash: kichik harflar va belgilarni olib tashlash"""
        text = text.lower()
        text = re.sub(r"[^a-zа-яё0-9\s\u0400-\u04FF]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text
    
    def predict_intent(self, text):
        """Matn asosida intent aniqlash."""
        text = self.preprocess(text)
        for intent, data in self.intents.items():
            for patt in data["patterns"]:
                if re.search(patt, text):
                    return intent
        return "unknown"
    
    def get_response(self, text):
        """Intentga mos javob qaytarish"""
        intent = self.predict_intent(text)
        response = random.choice(self.intents[intent]["responses"])
        # Log yozib qo'yamiz
        self.log_interaction(text, response)
        return response
    
    def log_interaction(self, user_text, agent_response):
        """Suhbat tarixini faylga yozib borish."""
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

