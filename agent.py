from groq_llm import chat_with_groq
from config import agent_config
from memory import Memory
import datetime

class Agent:
    def __init__(self):
        self.name = agent_config["name"]
        self.traits = ", ".join(agent_config["traits"])
        self.goal = agent_config["initial_goals"][0]
        self.memory = Memory()

    def current_time(self):
        return datetime.datetime.now().strftime("%H:%M")

    def decide_action(self):
        past = self.memory.recall("recent thoughts")
        with open("prompts/action.txt") as f:
            template = f.read()

        prompt = template.replace("{{name}}", self.name)\
                         .replace("{{traits}}", self.traits)\
                         .replace("{{time}}", self.current_time())\
                         .replace("{{goal}}", self.goal)\
                         .replace("{{memories}}", "\n".join(past))

        return chat_with_groq(prompt)

    def perform_action(self, action):
        print(f"🧠 {self.name} decided to: {action}")
        self.memory.store(f"{self.current_time()}: {action}")

    def reflect(self):
        past = self.memory.recall("what happened today")
        with open("prompts/thought.txt") as f:
            template = f.read()

        prompt = template.replace("{{name}}", self.name)\
                         .replace("{{memories}}", "\n".join(past))

        reflection = chat_with_groq(prompt)
        print(f"\n🪞 Reflection:\n{reflection}")
        self.memory.store(f"Reflection: {reflection}")
