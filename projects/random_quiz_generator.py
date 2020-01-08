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

	# TODO: Write out the header for the quiz.

	# TODO: Shuffle the order of the states.

	# TODO: loop through all 50 states, making a queston for each.
