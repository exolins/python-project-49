from brain_games.brain_calc import question_calc
from brain_games.brain_even import question_even
from brain_games.brain_progression import question_progression


def generate_question(game_name):
	match game_name:
		case 'even':
			return question_even()
		case 'calc':
			return question_calc()
		case 'progression':
			return question_progression()
		
