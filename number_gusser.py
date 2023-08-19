import random

low = 1
high = 50

correct_answer = random.randint(low, high)

for x in range(0,5):
    
        user_guess = int(input(f"Guess a number between {low} and {high}: "))
        
        if user_guess == correct_answer:
            print("Congratulations! You guessed the correct number.")
            print("Correct ancher is " , correct_answer)
            break
        elif user_guess < correct_answer:
            print("Correct answer is greater!")
            print("Correct ancher is " , correct_answer)
        else:
            print("Correct answer is less than!")
            print("Correct ancher is " , correct_answer)
    
        print("Please enter a valid number.")

print("You lose")