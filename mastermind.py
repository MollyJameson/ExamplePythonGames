import random

#These globals can be tuned for "fun factor"
_valid_chars = ['1','2','3','4','5','6','7']
_max_turns = 10

#Gamestate enums
STATE_GAMEPLAY = 0
STATE_WIN = 1
STATE_LOSE = 2

#Colored text unicode: BLACK,RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN
_text_colors = ['\033[90m','\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m']
ENDCOLOR = '\033[0m'

def GeneratePattern():
  pattern_len = 0
  #keep asking for input until it's in range
  while( pattern_len < 3 or pattern_len > 5):
    str_input = raw_input("How Long should the pattern be? (min 3, max 5): ")
    #verify it is a number
    if(str_input.isdigit()):
      pattern_len = int(str_input);
  #Copy all valid possibilities and shuffle in random order.
  #Don't just pick random indecies because Mastermind requires uniqueness
  used_chars = _valid_chars
  random.shuffle(used_chars)
  #Take first up to our max len
  _correct_pattern = used_chars[:pattern_len]
  return _correct_pattern;

def PlayerTurnGuess(turn_number,_correct_pattern):
  #print("DEV CHEAT!!! COMMENT ME out correct is " + "".join(_correct_pattern))
  str_input = raw_input("Turn: " + str(turn_number)+ " / " + str(_max_turns) +". Input guess (" +str(len(_correct_pattern))+ " digits): ")
  num_correct_in_place = 0
  num_contained_out_of_place = 0
  already_counted = []

  #Pick digits that are in correct place.
  min_len = min(len(str_input), len(str_input))
  for i in range(min_len):
    if(_correct_pattern[i] == str_input[i]):
      num_correct_in_place += 1
      already_counted.append(str_input[i])

  #only count a value as out of place iff
  #1. It wasn't counted correctly as "in place"
  #2. It wasn't counted before, that is the user inputted the same number twice
  for i in range(len(str_input)):
    if((not str_input[i] in already_counted) and str_input[i] in _correct_pattern):
        num_contained_out_of_place += 1
        already_counted.append(str_input[i])

  #Doing a colored output to be fancy not required... kind of confusing and should delete prob.
  colored_output = "";
  for i in range(len(str_input)):
    start_color = _text_colors[0]
    if(str_input[i].isdigit()):
      start_color = _text_colors[int(str_input[i]) % len(_text_colors)]
    colored_output += start_color + str_input[i] + ENDCOLOR
  print(colored_output)

  print("Digits in place: " + str(num_correct_in_place))
  print("Digits contained but out of place: " + str(num_contained_out_of_place))
  # newline for readability
  print("\n")
  if( num_correct_in_place == len(_correct_pattern)):
    raw_input("You Win! Press Enter to start a new game")
    return STATE_WIN;
  elif( turn_number >= _max_turns):
    raw_input("You Lose, out of turns! Answer was: " + "".join(_correct_pattern) + ". Press Enter to start a new game")
    return STATE_LOSE;
  else:
    return STATE_GAMEPLAY;

def StartNewGame():
  #Lame way to clear the screen for a new game
  print(' \n' * 25);
  print("Mastermind is a code guessing game.\nInput the correct combination with the clues given")
  _correct_pattern = GeneratePattern()
  state = STATE_GAMEPLAY
  turn_number = 0
  while(state == STATE_GAMEPLAY):
    turn_number += 1
    state = PlayerTurnGuess(turn_number,_correct_pattern)
  
#Main entry point.
#TODO: graceful quit.
while(True):
  StartNewGame()