"""Challenge Question 0: Functions"""

__author__ = "730736689"


def mimic(message: str) -> str:
    """Returns an identical message to the input."""
    return message


def main() -> None:
    """Main function to print results of mimic function."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
