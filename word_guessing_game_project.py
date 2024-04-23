import random
import time

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'watermelon',
             'mango', 'kiwi', 'peach', 'plum', 'cherry', 'blueberry', 'raspberry', 
             'papaya', 'lemon', 'lime', 'pear', 'fig', 'apricot', 'nectarine', 
             'dragonfruit', 'guava', 'lychee', 'passionfruit', 'cantaloupe', 'honeydew',
             'kiwifruit', 'tangerine', 'persimmon']
    return random.choice(words)

def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    level = input("Choose difficulty level (easy, medium, hard): ").lower()
    if level == "medium":
        attempts = 4
        time_limit = 45
    elif level == "hard":
        attempts = 3
        time_limit = 20
    else:
        time_limit = 60

    print("Welcome to the Word Guessing Game!")
    print("The word contains", len(word), "letters.")
    print("Hint: It's a fruit.")
    
    start_time = time.time()
    
    while attempts > 0:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, time_limit - elapsed_time)
        if elapsed_time > time_limit:
            print("Sorry, you ran out of time!")
            break

        guessed_word = ''
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += '_'
        print("Word:", guessed_word)
        print("Attempts left:", attempts)
        print("Time left:", round(remaining_time, 2), "seconds")
        
        if guessed_word == word:
            print("Congratulations! You guessed the word:", word)
            break
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
        else:
            guessed_letters.append(guess)
            if guess not in word:
                attempts -= 1
                print("Incorrect guess!")

    if attempts == 0:
        print("Sorry, you're out of attempts! The word was:", word)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time taken:", round(elapsed_time, 2), "seconds")

play_game()
