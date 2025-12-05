Test_Scores = [25, 50, 75]

# Creates a variable Max_score to test if the stored variable score is larger than the previous
Max_score = 0

# for loop that takes each score within Test_Scores and checks if the value is larger
# than Max_score. If it is, then it assigns score to Max_score
for score in Test_Scores:
    if score > Max_score:
        Max_score = score

print(Max_score)