import random

#These globals can be tuned for "fun factor"
_valid_chars = ['1','2','3','4','5','6','7','8','9']
_max_turns = 12

#Gamestate enums
STATE_GAMEPLAY = 0
STATE_WIN = 1
STATE_LOSE = 2
STATE_QUIT = 3

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

  print("Digits in place: " + str(num_correct_in_place))
  print("Digits contained but out of place: " + str(num_contained_out_of_place))
  # newline for readability
  print("\n")
  if( num_correct_in_place == len(_correct_pattern)):
    end_input = raw_input("You Win! Would you like to play again (Y/N)?")
    if( 'n' in end_input.lower() ):
      return STATE_QUIT
    return STATE_WIN;
  elif( turn_number >= _max_turns):
    end_input = raw_input("You Lose, out of turns! Answer was: " + "".join(_correct_pattern) + ". Would you like to play again (Y/N)?")
    if( 'n' in end_input.lower() ):
      return STATE_QUIT
    return STATE_LOSE;
  else:
    return STATE_GAMEPLAY;

def StartNewGame(state):
  #Lame way to clear the screen for a new game
  print(' \n' * 25);
  print("Mastermind is a code guessing game.\nInput the correct combination with the clues given")
  _correct_pattern = GeneratePattern()
  turn_number = 0
  while(state == STATE_GAMEPLAY):
    turn_number += 1
    state = PlayerTurnGuess(turn_number,_correct_pattern)
  return state
  
#Main entry point.
state = STATE_GAMEPLAY
while(state != STATE_QUIT):
  state = StartNewGame(STATE_GAMEPLAY)