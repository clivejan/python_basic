my_skills = ["Linux", "AWS", "Python", 'Ansible', 'Jenkins']

skill = input("Enter a skill name: ")
if skill not in my_skills:
	print(f'I do not have the skill of {skill} yet, but I will work on it.')
else:
	print(f"I do have the knowledge about {skill}.")
