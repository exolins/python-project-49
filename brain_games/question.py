from brain_games.brain_calc import question_calc
from brain_games.brain_even import question_even


def generate_question(game_name):
	match game_name:
		case 'even':
			return question_even()
		case 'calc':
			return question_calc()
		
