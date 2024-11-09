

from speakly import Speakly


speakly = Speakly(scenario="You are a drivethru worker at mcdonalds, ", language="french")
while True:
    text = input("Talk:")
    print(speakly.sendMessage(text))