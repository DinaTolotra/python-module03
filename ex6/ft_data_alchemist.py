import random


if __name__ == "__main__":
    mixed_list: list[str]
    filtered_list: list[str]
    transformed_list: list[str]
    score: dict[str, int]
    avg_score: float
    high_score: dict[str, int]

    mixed_list = [
        "Alice", "bob", "Charlie",
        "dylan", "Emma", "Gregory",
        "john", "kevin", "Liam"
    ]
    filtered_list = [
        name for name in mixed_list if name[0].isupper()
    ]
    transformed_list = [
        name.capitalize() for name in mixed_list
    ]
    print("Initial list of players:", mixed_list)
    print("New list with all names capitalized:", transformed_list)
    print("New list of capitalized names only:", filtered_list)
    score = {name: random.randint(0, 1000) for name in transformed_list}
    avg_score = round(sum(score.values()) / len(score), 2)
    high_score = {key: val for key, val in score.items() if val > avg_score}
    print("Score dict:", score)
    print("Score average is", avg_score)
    print("High scores:", high_score)
