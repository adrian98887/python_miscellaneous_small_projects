#Black Jack

import random 
from replit import clear

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(list):
  """Takes a list of cards and returns the score. Or a 0 if it's a Black Jack."""
  if sum(list) == 21 and len(list) == 2:
    return sum(list)
  elif sum(list) > 21 and 11 in list:
    list.remove(11)
    list.append(1)
  return sum(list)

def compare(user_score, dealer_score):
  """Compares two scores together and returns an appropriate message."""
  if user_score == dealer_score:
    print("It's a draw!")
  elif dealer_score == 21:
    print("You lose!")
  elif user_score == 21:
    print("You win!")
  elif user_score > 21:
    print("You lose!")
  elif dealer_score > 21:
    print("You win!")
  else:
    if user_score > dealer_score:
      print("You win!")
    else:
      print("You lose!")

def play_game():
  keep_playing = True
  player_list = []
  dealer_list = []
  
  for card in range(2):
    player_list.append(deal_card())
    dealer_list.append(deal_card())
  
  while keep_playing is True:
    player_score = calculate_score(player_list)
    dealer_score = calculate_score(dealer_list)
    print(f"Your cards are {player_list}, current score: {player_score}")
    print(f"Dealers first card is {dealer_list[0]}")
    if player_score == 0 or dealer_score == 0 or player_score > 21 or player_score == 21:
      #print(f"Dealer Wins! With cards {dealer_list}, current score: {dealer_score}")
      keep_playing = False
    else:
      if input("Do you want to draw another card? Type 'y' or 'n' ") == 'y':
        player_list.append(deal_card())
        player_score = calculate_score(player_list)
      else:
        keep_playing = False
  
  while dealer_score < 17:
    dealer_list.append(deal_card())
    dealer_score = calculate_score(dealer_list)
    if dealer_score == 21:
      print("The dealer has won!")
    
  compare(player_score,dealer_score)
  
  print(f"Your cards are {player_list}, current score: {player_score}")
  print(f"Dealers cards are {dealer_list}, dealers score: {dealer_score}")


if input("Do you want to play black jack? Type 'y' or 'n' ") == 'y':
  play_game()
else:
  exit()

while input("Do you want to play another game? Type 'y' or 'n' ") == 'y':
  clear()
  play_game()
