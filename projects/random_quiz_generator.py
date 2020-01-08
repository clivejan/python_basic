#!/usr/bin/env python3
# random_quiz_generator.py - Creates quizzes with questions and answers
# in random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capotals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 
'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier',
'Virginia': 'Richmond', 'Washington': 'Olympia','WestVirginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quiz_num in range(35):
	# Create the quzi and answer key files.
	quiz_file = open(f'capitals_quiz_{quiz_num+1}.txt', 'w')
	answer_key_file = open(f'capitals_answer_{quiz_num+1}.txt', 'w')

	# Write out the header for the quiz.
	quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
	quiz_file.write(f"{' '*20} State Capitals Quiz (Form {quiz_num+1})")
	quiz_file.write('\n\n')

	# Shuffle the order of the state.
	states = list(capitals.keys())
	random.shuffle(states)

	# Loop through all 50 states, making a queston for each.
	for question_num in range(50):
		# Get right and wrong answers.
		corrent_answer = capitals[states[question_num]]
		wrong_answers = list(capitals.values())
		del wrong_answers[wrong_answers.index(corrent_answer)]
		wrong_answers = random.sample(wrong_answers, 3)
		answer_options = wrong_answers + [corrent_answer]
		random.shuffle(answer_options)

		# Write the question and the answer options to the quiz file.
		quiz_file.write(f"{question_num+1}. What is the capitals of "
			f"{states[question_num]}\n")
		for i in range(4):
			quiz_file.write(f"\t{'ABCD'[i]}. {answer_options[i]}")
		quiz_file.write('\n')

		# Write the answer key to a file
		answer_key_file.write(f"{question_num+1}. "
			f"{'ABCD'[answer_options.index(corrent_answer)]}\n")

	quiz_file.close()
	answer_key_file.close()
