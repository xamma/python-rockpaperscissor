from game_class import RockPaperScissor

def execute():
  RPSObject = RockPaperScissor()
  play_again = True
  while play_again:
    RPSObject.greet_user()
    user_input = RPSObject.get_user_input()
    if user_input == 4:
      play_again = False
    computer_choice = RPSObject.get_computer_choice()
    RPSObject.calculate_winner(user_input, computer_choice)

if __name__ == "__main__":
  execute()