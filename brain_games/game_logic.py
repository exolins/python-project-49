import brain_games.game_cli as bg_cli
from brain_games.question import generate_question


def answer_check(answer_user, answer_right):
    return answer_user == answer_right


def game_round(game_name, user_name):
    question, answer_right = generate_question(game_name)
    bg_cli.question_show(question)
    answer_user = bg_cli.answer_prompt()
    if answer_check(answer_user, answer_right):
        bg_cli.round_win_show()
        return True
    else:
        bg_cli.round_lost_show(answer_user, answer_right, user_name)
        return False 


def game(game_name, user_name):
    count_round_win = 0
    bg_cli.game_welcome_show(game_name)
    while count_round_win < 3:
        if game_round(game_name, user_name):
            count_round_win += 1
        else:
            count_round_win = 0
    bg_cli.game_win_show(user_name)
    


