"""Practicing recursion with a tea party scenario."""

__author__ = "730736689"


def main_planner(guest: int) -> None:
    """Main functions for planning the tea party."""
    print("A Cozy Tea Party for " + str(guest) + " People!")
    print("Tea Bags: " + str(tea_bags(guest)))  # use guest number as input for people
    print(
        "Treats: " + str(treats(guest))
    )  # same: guest as input for treats, will call the tea_bags function inside
    print(
        "Cost: $" + str(cost(tea_bags(guest), treats(guest)))
    )  # use cost function w/ guest and tea_bags/treats, not the exact cost function


def tea_bags(people: int) -> int:
    """Calculates how many tea bags are needed if each person has two."""
    return 2 * people


def treats(people: int) -> int:
    """Calculates how many treats are needed 1.5 treats accompany one tea."""
    return int(
        1.5 * tea_bags(people=people)
    )  # nest the tea_bags function inside treats for simpler calculation


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea bags and treats."""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guest=int(input("How many guests are attending your tea party?")))
