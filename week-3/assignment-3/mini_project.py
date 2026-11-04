# 3-Day Holiday Weekend Planner

day = input("What day is it? ").lower()
time_of_day = input("What time of day? ").lower()

if day == "saturday" and time_of_day == "morning":
    print("Suggestion: Go on a morning run! ")
elif day == "saturday" and time_of_day == "afternoon":
    print("Suggestion: Go to a Saturday brunch! ")
elif day == "saturday" and time_of_day == "evening":
    print("Suggestion: Relax and watch a movie. ")
elif day == "sunday" and time_of_day == "morning":
    print("Suggestion: Go to church. ")
elif day == "sunday" and time_of_day == "afternoon":
    print("Suggestion: Clean your house or do laundry. ")
elif day == "sunday" and time_of_day == "evening":
    print("Suggestion: Cook Sunday dinner. ")
elif day == "monday" and time_of_day == "morning":
    print("Suggestion: Go to the gym for your Monday morning workout! ")
elif day == "monday" and time_of_day == "afternoon":
    print("Suggestion: Take a trip to the grocery store. ")
elif day == "monday" and time_of_day == "evening":
    print("Suggestion: Time to wind down! ")
else:
    print("Sorry, I don't recognize that day. Try: Saturday, Sunday, Monday... ")
