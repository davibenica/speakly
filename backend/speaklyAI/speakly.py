from os import system
from openai import OpenAI


class Speakly:

    def __init__(self, scenario, language):
        self.client = OpenAI()
        self.scenario = scenario
        self.language = language
        self.prompt = "you are having a conversation with a beginner in" + self.language +  " you will be given a scenario, and i want you to have a conversation with the user in" + self.language + "I only want you to speak with the user in this language no other one. This is the senario "+ self.scenario 
        self.message_history = []
        self.message_history.append({"role": "system", "content": self.prompt})

    def sendMessage(self, text):
        self.message_history.append({"role":"user",
                                     "content": text})
        completion = self.client.chat.completions.create(
        model="gpt-4o",
        messages=self.message_history
    )
        response = completion.choices[0].message.content
        self.message_history.append({"role": "system", "content": response})
        return response
    
    def getUserResponses(self):
        userMesseges= []
        for message in self.message_history:
            if message["role"] == "user":
                userMesseges.append(message)
        return userMesseges

    def getSystemResponses(self):
        systemMesseges= []
        for message in self.message_history:
            if message["role"] == "system":
                systemMesseges.append(message)
        return systemMesseges 


        
        

        
