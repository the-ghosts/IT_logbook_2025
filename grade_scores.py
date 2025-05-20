def grade_score(score):
	if score >= 70:
		return "A"
	elif score >=60 and score <= 69:
		return "B"
	elif score >= 50 and score <= 59:
		return "C"
	elif score >=45 and score <= 49:
		return "D"
	else:
		return "F"


if __name__ == "__main__":
	score = int(input("Enter your score: "))
	grade = grade_score(score)
	print(f"Your grade is: {grade}")
