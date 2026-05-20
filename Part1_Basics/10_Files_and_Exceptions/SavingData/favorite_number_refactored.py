from pathlib import Path
import json

def get_stored_number(path):
  """Get stored favorite number if available."""
  if path.exists():
    contents = path.read_text()
    fav_num = json.loads(contents)
    return fav_num
  else:
    return None
  
def get_new_number(path):
  """Prompt for a new favorite number, if one does not already exist."""
  fav_num = input("What's your favorite number? ")
  contents = json.dumps(fav_num)
  path.write_texts(contents)
  return fav_num

def favorite_number():
  path = Path('fav_num.json')
  fav_num = get_stored_number(path)
  if fav_num:
    print(f"I know your favorite number! It is {fav_num}!")
  else:
    fav_num = get_new_number(path)

favorite_number()