'''
word guessing game
'''

key_word = "PASSWORD"
trials =4
count = 0
while count < trials:
    word_guesses = input("Enter your guess ")
    count += 1

    if word_guesses.upper() == key_word:
        print("Congratulations! You guessed it right in ", count, "trials")
        break
        print()

    else:
        print("Sorry ", trials-count, "tries remaining")
        print()

if count >= trials:
    print("The answer was ", key_word, "Best of Luck next time")