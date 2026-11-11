def is_valid_score(score):
    return isinstance(score, int) and 0 <= score <= 100

score = int(input("Enter your score: "))
if is_valid_score(score):

    print("Valid score. ")
else:
    print("Invaild score - must be between 0 and 100. ")