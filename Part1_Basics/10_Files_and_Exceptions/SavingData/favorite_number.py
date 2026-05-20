# Prompt for user's favorite number. Use json.dumps() to save this. Read in the value.

from pathlib import Path
import json

def favorite_number():
  path = Path('fav_num.json')
  if path.exists():
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f"I know your favorite number! It's {fav_num}!")
  else:
    fav_num = input("What's your favorite number? ")
    contents = json.dumps(fav_num)
    path.write_text(contents)
    print(f"I know your favorite number! It's {fav_num}!")

favorite_number()