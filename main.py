import random

word_choices = [
    "fluff",
    "crate",
    "decks",
    "faint",
    "bring",
    "crash",
    "prone"
]

def get_guess():
    guess = []
    for i in range(5):

        while True:
            letter = input('letter: ').lower().strip()

            if letter.isalpha() and len(letter) == 1:
                break

        guess.append(letter)
    return guess

def evaluate_status(correct_word_list, guess_list):
    guess_status = []
    for index in range(len(correct_word_list)):
        if guess_list[index] == correct_word_list[index]:
            guess_status.append('correct')
        elif guess_list[index] in correct_word_list:
            guess_status.append('contains')
        else:
            guess_status.append('incorrect')
    return guess_status

def main():

    correct_word_list = list(random.choice(word_choices))
    print(correct_word_list)
    guess_history = []
    guess_history_status = []
    guesses = 6

    while guesses > 0:
        print()
        
        guess_list = list(get_guess())
        guess_history.append(guess_list)
        guess_status = evaluate_status(correct_word_list, guess_list)
        guess_history_status.append(guess_status)
        
        print(f'guess_history: {guess_history}')
        print(f'guess_history_status: {guess_history_status}')

        guesses -= 1

main()