from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
  emoji: str
  sentiment: float

def get_mood(input_text: str,*,sensitivity: float) -> Mood:
  polarity: float = TextBlob(input_text).sentiment.polarity

  friendly_threashold: float = sensitivity
  hostile_threashold: float = -sensitivity
  if polarity >= friendly_threashold:
    return Mood('😊',polarity)
  elif polarity < hostile_threashold:
    return Mood('😡',polarity)
  else:
    return Mood('😐',polarity)

def run_bot():
  print('Enter text to get sentiment analysis: ')
  while True:
    user_input:str = input('YOU: ')
    mood: Mood = get_mood(user_input,sensitivity=0.3)
    print(f'BOT: {mood.emoji} ({mood.sentiment})')

if __name__ == '__main__':
  run_bot()