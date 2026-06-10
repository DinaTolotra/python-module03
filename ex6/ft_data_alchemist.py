import random


if __name__ == "__main__":
    mixed_list: list[str] = [
        "Alice", "bob", "Charlie",
        "dylan", "Emma", "Gregory",
        "john", "kevin", "Liam"
    ]
    filtered_list: list[str] = [
        name for name in mixed_list if name[0].isupper()
    ]
    transformed_list: list[str] = [
        name.capitalize() for name in mixed_list
    ]
    print("Initial list of players:", mixed_list)
    print("New list with all names capitalized:", transformed_list)
    print("New list of capitalized names only:", filtered_list)
    score: dict[str, int] = {
        name: random.randint(0, 1000) for name in transformed_list
    }
    avg_score: float = round(sum(score.values()) / len(score), 2)
    high_score: dict[str, int] = {
        key: val for key, val in score.items() if val > avg_score
    }
    print("Score dict:", score)
    print("Score average is", avg_score)
    print("High scores:", high_score)
