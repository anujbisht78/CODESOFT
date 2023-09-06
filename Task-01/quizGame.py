"""Quiz Game"""

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        print(f"{answer} is the Correct Answer!")
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    ans=[]
    for i in questions:
        print(questions.get(i), end=" ")
        ans.append(questions.get(i))
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score=0
    i=0
    j=0
    while i<len(ans) and j<len(guesses):
        if ans[i]==guesses[j]:
            score+=1
        i+=1
        j+=1
    print("Your score is: ",score)

def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
 "1. Who created Python?: ": "A",
 "2. What year was Python created?: ": "B",
 "3. Python is tributed to which comedy group?: ": "C",
 "4. Nuclear sizes are expressed in a unit named: ": "A",
 "5. Light year is a unit of: ": "B",
 "6. What is part of a database that holds only one type of information?: ": "B",
 "7. 'OS' computer abbreviation usually means ?: ": "C",
 "8. '.MOV' extension refers usually to what kind of file?: ": "B",
 "9. The percentage of irrigated land in India is about: ": "C",
 "10. The southernmost point of peninsular India, that is, Kanyakumari, is: ": "D"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. Fermi","B. angstrom", "C. newton", "D. tesla"],
          ["A. time","B. distance", "C. light", "D. intensity of light"],
          ["A. Report","B. Field", "C. Record", "D. File"],
          ["A. Order of Significance","B. Open Software", "C. Operating System", "D. Optical Sensor"],
          ["A. Image file","B. Animation/movie file", "C. Audio file", "D. MS Office document"],
          ["A. 45","B. 65", "C. 35", "D. 25"],
          ["A. north of Tropic of Cancer","B. south of the Equator", "C. south of the Capricorn", "D. north of the Equator"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")
