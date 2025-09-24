# Simple AI Agent (Chatbot)

This is a beginner-friendly **AI Agent (Chatbot)** project built with Python.  
The chatbot uses a simple **intents.json** file to handle predefined questions and answers.  

---

## Features
- Responds to predefined intents (greetings, help, goodbye, etc.)
- Easy to extend by adding more intents in `intents.json`
- Beginner-friendly structure
- Pure Python implementation (no heavy dependencies)

---

## Project Structure
```
ai_agent_project/
│── intents.json        # Contains intents and responses
│── agent.py            # Main chatbot logic
│── README.md           # Project documentation
```


---

## Example Run
```bash
$ python agent.py
You: hi
Agent: Hello! How can I help you?

You: goodbye
Agent: Goodbye! Have a nice day!
```

## How to Add New Intents

- Open intents.json
- Add a new intent with patterns and responses:

---

```
{
  "tag": "thanks",
  "patterns": ["thanks", "thank you", "thx"],
  "responses": ["You're welcome!", "No problem!", "Glad I could help!"]
}
```

- Run the chatbot again and test.

## Installation & Usage

- Clone the repository:
```
git clone https://github.com/username/repository_name.git
cd repository_name
```
- Run the chatbot:
```
python rule_based_agent.py
```

## Future Improvements

- Add NLP model for smarter responses
- Integrate with APIs (weather, news, etc.)
- Build a GUI or web version
