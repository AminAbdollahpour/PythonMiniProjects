print("Hello and Wellcome to QuizGame!")
permission = input("Do you wish to play? ").lower()
if permission != "yes":
    print("Come back anytime,Goodbye.")
    quit()

print("So here we go,Lets start.")
score = 0
#q1

question = input("What does CPU stand for? ").lower()
if question == "central processing unit":
    print("ur goddam right!")
else:
    print("try harder next time.")
#q2

question = input("What does DOTA stand for? ").lower()
if question == "defence of the ancients":
    print("ur goddam right!")
    score += 1
else:
    print("try harder next time.")
#q3

question = input("Is earth flat?(answer in Yes or No) ").lower()
if question == "no":
    print("ur goddam right!")
    score += 1
else:
    print("flat earth isn't real it can't heart you.")
#q4

question = input("What the dog doing? ").lower()
if True:
    print("doing ur mom :)")
#q5

question1 = input("Why did SteveJobs died? ").lower()
if question1 == "ligma":
    print("lig ma balls")
    score += 1
else:
    print("You touch grass once in a while that's good.")


print("That's the end of questions.")
result = input("Would you like to check your score? ").lower()
if result == "yes":
    print("Your score is "+str(score)+". ")
else:
    print("Goodbye come back anytime.")
    quit()
print("It was fun come back again.")
