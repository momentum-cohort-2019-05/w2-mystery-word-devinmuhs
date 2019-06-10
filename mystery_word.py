def guess_taker():
    import random
    f = open("common_words.txt")
    all_words = (f.read()).upper()


    split_all_words = all_words.split()

    easy_words = []
    normal_words = []
    hard_words = []
    for word in split_all_words:
        if len(word) >= 8:
            hard_words.append(word)
        elif len(word) >= 6 and len(word) <= 8:
            normal_words.append(word)
        elif len(word) <= 6 and len(word) >= 4:
            easy_words.append(word)


    difficulty_selector = input("Welcome to the Myster Word Game!\n\nPlease enter your difficulty level:\n\nEASY\nNORMAL\nHARD\n>> ")
    upper_case_difficulty = difficulty_selector.upper()

    while upper_case_difficulty not in ["EASY", "NORMAL", "HARD"]:
        print("INVALID ENTRY: Please try again!")
        difficulty_selector = input("Welcome to the Myster Word Game!\n\nPlease enter your difficulty level: \n\nEASY\nNORMAL\nHARD\n>> ")
        upper_case_difficulty = difficulty_selector.upper()


    if upper_case_difficulty == "EASY":
        word = random.choice(easy_words)
    elif upper_case_difficulty == "NORMAL":
        word = random.choice(normal_words)
    elif upper_case_difficulty == "HARD":
        word = random.choice(hard_words)
    

    print("This word is",len(word),"characters long")
    current_guesses= []

    def display_letter(letter, guesses):
        """
        Conditionally display a letter. If the letter is already in
        the list `guesses`, then return it. Otherwise, return "_".
        """
        if letter in guesses:
            return letter
        else:
            return "_"

    def print_word(word, guesses):
        output_letters = []
        for letter in word:
            output_letters.append(display_letter(letter, guesses))
        return (" ".join(output_letters))


    word_match = word.replace("", " ")
    word_match = word_match.strip()    
    guess_counter = 8
    # print(word_match)
    print("Lives remaining: ", guess_counter)
    guess = input("Please input your letter guess: ").upper()

    
    wordGuessed = False

    while guess_counter > 0 and wordGuessed is False:
        if guess in current_guesses:
            print("INVALID ENTRY! Already been guessed!")
        if len(guess) != 1 or guess.isalpha() == False:
            print("ERROR! Please enter one letter.")
        if guess in word and len(guess) == 1 and guess not in current_guesses:
            print("Correct!", guess, "is in the word!")
            if guess not in current_guesses and len(guess) == 1:
                current_guesses.append(guess)
                if word_match == print_word(word, current_guesses):
                    wordGuessed is True
                    print(print_word(word, current_guesses))
                    print("Congrats! You beat the game! The word was", word)
                    break
        if guess not in word and guess not in current_guesses and guess.isalpha() == True and len(guess) == 1:
            print("Sorry,", guess, "is not in the word.")
            current_guesses.append(guess)
            guess_counter -= 1

        if guess_counter > 0:
            print(print_word(word, current_guesses))
            print("Current guesses: ", current_guesses)
            print("Lives remaining: ", guess_counter, "\n")
            guess = input("Please input your letter guess: ").upper()

    if guess_counter == 0:
        print("GAME OVER! The word was", word.upper())
    end_game = input("Play again?\n1- Yes\n2- No\n>> ")
    end_game = end_game.lower()

    if end_game == "yes" or end_game == "y" or end_game == "1":
        guess_taker()
    else:
        print("Good-bye!")

guess_taker()