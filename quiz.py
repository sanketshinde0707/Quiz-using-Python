Questions = []

score = 0
n = int(input("Enter the number of questions to be entered in the array\n"))

"""This is the loop for adding questions and there options"""
for i in range(n):
    Question = {}
    question = input("Enter the " + str(i) + "th question\n")
    option1 = input("Enter the option 1\n")
    option2 = input("Enter the option 2\n")
    option3 = input("Enter the option 3\n")
    option4 = input("Enter the option 4\n")
    answer = input("Enter the correct option in the following format (e.g option1 )")
    Question["question"] = question
    Question["option1"] = option1
    Question["option2"] = option2
    Question["option3"] = option3
    Question["option4"] = option4
    Question["correctAnswer"] = answer
    Questions.append(Question)

"""This loops displays the questions and there options to the user , also it takes the user answer ,and stores the score of the user """
for obj in Questions:
    print(obj)
    print(obj["question"])
    print(obj["option1"])
    print(obj["option2"])
    print(obj["option3"])
    print(obj["option4"])
    answer = input("Enter the correct option no in this format (e.g option1 )")
    obj["userAnswer"] = answer
    if obj["userAnswer"] == obj["correctAnswer"]:
        score += 1

print("The score is ",score)
