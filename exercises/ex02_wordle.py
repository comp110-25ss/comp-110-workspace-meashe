"""A wordle-based game for practicing functions and lists."""

__author__ = "730736689"


def main(secret: str) -> None:
    """The entrypoint of the program and the main game loop"""
    turn: int = 1
    while turn <= 6:
        print(str("===Turn " + str(turn) + "/6==="))
        answer = input_guess(N=len(secret))
        # calls on input function, allows result to be used
        print(emojified(guess=answer, secret=secret))
        if answer == secret:
            print("You won in " + str(turn) + "/6 turns!")  # winning result
            turn = 7  # finished while loop
        else:
            if turn == 6:
                print("X/6 - Sorry, try again tomorrow!")
                turn += 1  # finishes while loop
            else:
                turn += 1  # moves on while loop


def contains_char(word: str, character: str) -> bool:
    """A function that searches for a character in a word."""
    assert len(character) == 1, f"len('{character}') is not 1"
    word_idx: int = 0  # create variable to iterate along string
    while word_idx < len(word):
        if word[word_idx] == character:
            return True
        word_idx += 1  # move along while loop
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis codifying the results of a guess."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    white_box: str = "\U00002b1c"
    green_box: str = "\U0001f7e9"
    yellow_box: str = "\U0001f7e8"
    guess_idx: int = 0
    secret_idx: int = 0  # create these two variables to determine beyond the contain fn
    emojis: str = ""  # empty string to begin
    while guess_idx < len(guess):
        if contains_char(word=secret, character=guess[guess_idx]) is True:
            if guess[guess_idx] == secret[secret_idx]:
                emojis = emojis + green_box  # to change "emojis", emojis must = new str
            else:
                emojis = emojis + yellow_box
        else:
            emojis = emojis + white_box
        guess_idx += 1
        secret_idx += 1
    return emojis


def input_guess(N: int) -> str:
    answer: str = input("Enter a " + str(N) + " character word:")
    while len(answer) != N:
        answer = input("That wasn't " + str(N) + " chars! Try again:")
        # change the answer variable to have new input
    return answer


if __name__ == "__main__":
    main(secret="codes")
