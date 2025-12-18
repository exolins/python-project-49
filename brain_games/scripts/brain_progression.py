from brain_games.game_cli import prompt_user_name, welcome_to_brain_games
from brain_games.game_logic import game

# progression


def main():
    welcome_to_brain_games()
    user_name = prompt_user_name()
    game('progression', user_name)    
    



