from secrets import randbelow
from enum import Enum

class Options(Enum):
  ROCK = 1
  PAPER = 2
  SCISSOR = 3

class RockPaperScissor:
  def __init__(self) -> None:
    pass

  def get_user_input(self):
    x = int(input())
    return x

  def greet_user(self):
    print("Hello ! Time to play. ")
    print("Please insert your choice")
    print("(1) Rock")
    print("(2) Paper")
    print("(3) Scissor")
    print("-----------")
    print("Enter '4' to quit the game")

  def get_computer_choice(self):
    choice = randbelow(4)
    while choice == 0:
      choice = randbelow(4)
    return choice

  def get_answer(self, human_choice, computer_choice):
    if human_choice == 1:
      human_choice = Options.ROCK.name
      print(f"You chose {human_choice}.")
    elif human_choice == 2:
      human_choice = Options.PAPER.name
      print(f"You chose {human_choice}.")
    elif human_choice == 3:
      human_choice = Options.SCISSOR.name
      print(f"You chose {human_choice}.")
    else:
      print("Please choose a valid option.")
    if computer_choice == 1:
      computer_choice = Options.ROCK.name
      print(f"Computer chose {computer_choice}.")
    elif computer_choice == 2:
      computer_choice = Options.PAPER.name
      print(f"Computer chose {computer_choice}.")
    elif computer_choice == 3:
      computer_choice = Options.SCISSOR.name
      print(f"Computer chose {computer_choice}.")
    else:
      print("Please choose a valid option.")

  def print_tie(self):
    print("Tie! Noone wins, try again.")

  def print_win(self):
    print("You won! Congratulations.")

  def print_lose(self):
    print("You lose!")
    
  def calculate_winner(self, human_choice, computer_choice):
    if human_choice == computer_choice:
      self.get_answer(human_choice=human_choice, computer_choice=computer_choice)
      self.print_tie()
    elif human_choice == Options.ROCK.value and computer_choice == Options.PAPER.value:
      self.print_lose()
      self.get_answer(human_choice=human_choice, computer_choice=computer_choice)
    elif human_choice == Options.ROCK.value and computer_choice == Options.SCISSOR.value:
      self.get_answer(human_choice=human_choice, computer_choice=computer_choice)
      self.print_win()
    elif human_choice == Options.PAPER.value and computer_choice == Options.SCISSOR.value:
      self.get_answer(human_choice=human_choice, computer_choice=computer_choice)
      self.print_lose()
    elif human_choice == Options.PAPER.value and computer_choice == Options.ROCK.value:
      self.get_answer(human_choice=human_choice, computer_choice=computer_choice)
      self.print_win()
    elif human_choice == Options.SCISSOR.value and computer_choice == Options.ROCK.value:
      self.get_answer(human_choice=human_choice, computer_choice=computer_choice)
      self.print_lose()
    elif human_choice == Options.SCISSOR.value and computer_choice == Options.PAPER.value:
      self.get_answer(human_choice=human_choice, computer_choice=computer_choice)
      self.print_win()
    elif human_choice == 4:
      print("Goodbye !")
    else:
      print("Please choose a valid option.")