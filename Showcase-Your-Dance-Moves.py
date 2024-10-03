# Author: Silas Leone
# Date: October 3, 2024
# Task 1: Correct Indents - I added proper indents for the print statements.

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")
    
# Task 2: Your Mood Today: Ask the user how they feel today. If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!". 
while True:
    mood_today = input("How do you feel today? (Happy / Sad): ").lower()
    if mood_today == "happy":
        print("That's great to hear!")
    elif mood_today == "sad":
        print("I hope your day gets better!")
    else:
        print("Invalid entry, try again.")
        continue