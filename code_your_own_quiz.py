#Code your own quiz python 2



#Welcome to my code your own quiz, you need to fill in the blanks

#This print welcome message and ask for categories
print "Welcome to my quiz game!"

print "Type your quiz catagory!"
print "Choose: Easy, Medium or Hard"
level = raw_input ("level_select:Easy, Medium, Hard ")

gaps = ["__1__", "__2__", "__3__", "__4__"]

answers_easy =["London", "Edinburgh", "Belfast" ,"Cardiff"]
text_easy = "The capital of England is __1__ . The capital city of Scotland is __2__. The capital city of Northen Ireland is  __3__. The capital of Wales is called __4__. Together these countries form The United Kingdom."

answers_medium = ["Norway", "Sweden", "Denmark" ,"Finland"]
text_medium = "There is an area of the world called the Nordics. It consists of four countries. Oslo is the capital city of __1__. Stockholm is the capital city of __2__. Copenhagen is the capital city of __3__. Helsinki is the capital of __4__." 

answers_hard =["Ottawa", "Canberra", "Brasilia", "Bern"]
text_hard = ["The capital city of Canada is __1__, The capital city of Australia __2__.  The capital of Brazil is __3__. The capital of switzerland is __4__."]


def level_select (level):
	""" Takes user input from Easy, Medium or and loads correct text based on level selection"""
	if level == "Easy":
	    return text_easy, answers_easy
	elif level == "Medium":
		return text_medium, answers_medium
	elif level == "Hard":
		return text_hard, answers_hard
	else: 
		print "Bad news, try again."

	quiz,answers = level_select(level)




def check_answer(user_input, answers, answer_index):
	""" Checks and responds to inputs user_input, answers, answer_index). If answer matches user input returns Well done, else try again."""
	if user_input==answers[answer_index]:
		return "Well done"
	return "Try again"


def replace_gaps(gaps, answer, quiz):
	""" Replace the blank spaces with the correct answers, takes inputs from gaps, answer and quiz and outputs quiz"""
	quiz = quiz.replace(gaps, answer)
	return quiz


def start_quiz(gaps):
	"""Begin the quiz of all quizes, prints quiz questions, responds Try Again or Well done,depending on which input is received. This function also alows the game to move along to the next question segment """
	quiz,answers= level_select(level)
	print quiz
	blank_index = 0
	answer_index = 0
	while blank_index<len(gaps):
		user_input=raw_input ("The answer for " +  gaps[blank_index])
		while check_answer(user_input, answers, answer_index)=="Try again":
			user_input=raw_input("Try again" + gaps[blank_index])
		if check_answer(user_input, answers, answer_index)=="Well done":
			print "Sweet, well done"
			quiz = replace_gaps(gaps[blank_index], answers[answer_index], quiz)
			print quiz
			blank_index +=1
			answer_index +=1



start_quiz(gaps)
