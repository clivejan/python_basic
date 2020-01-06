skills_name = []

while True:
	skill_name = input(f"Enter the name of skill {len(skills_name) + 1} "
		"(Or enter nothing to stop): ")

	if skill_name == "":
		break
	skills_name = skills_name + [skill_name]

print("The skill names are:")
for name in skills_name:
	print(f"\t{name}")
