import random
from gtts import gTTS


responses = list()


with open('insults.txt', 'r') as f:
  for line in f:
      responses.append(line)

responses.sort()

def myfunc(name):
  x = random.choice(responses)
  print(x)
  tts = gTTS(text=x, lang='en')
  tts.save("insult.mp3")



while True:
  myfunc(input("Name: "))
