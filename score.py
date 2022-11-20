SCORE_MIN = 0
SCORE_MID = 50
SCORE_HIGH = 90
SCORE_MAX = 100

score = float(input("Enter score: "))
if SCORE_MIN < score < SCORE_MID:
    level = "Bad"
elif score < SCORE_HIGH:
    level = "Pass"
elif score < SCORE_MAX:
    level = "Excellent"
else:
    level = "Invalid score"

print(level)

