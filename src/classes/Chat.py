import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path=env_path)
max_tokens = 4096
reserve_messages = 3 

# Set up your OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

class Chat:
    def __init__(self, opening_message="Your goal is to examine data from the user and respond with what they ask"):
        self.messages = [
            {"role": "system", "content": opening_message}
        ]

    def _count_tokens(self):
        return sum(len(message["content"].split()) for message in self.messages)

    def ask(self, user_text):
        self.messages.append({"role": "user", "content": user_text})

        # Cap message length
        while self._count_tokens() > max_tokens:
            if len(self.messages) > reserve_messages:
                self.messages.pop(reserve_messages) 
            else:
                break

        try:
            response = client.chat.completions.create(
                model="gpt-4o",  # or "gpt-4" if you have access
                messages=self.messages
            )
            reply = response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            return f"Error: {e}"