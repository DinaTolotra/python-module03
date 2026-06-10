import random


def get_achievements() -> set[str]:
    return {
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
        "Hidden Path Finder",
    }


def gen_player_achievements() -> set[str]:
    achievements: list[str] = list(get_achievements())
    achiev_count: int = len(achievements)
    gen_count: int = random.randrange(0, achiev_count)

    return set(random.sample(achievements, k=gen_count))


if __name__ == "__main__":
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)
    print("")

    print("All distinct achievements:",
          alice.union(bob).
          union(charlie).
          union(dylan),
          "\n")

    print("Common achievements:",
          alice.intersection(bob).
          intersection(charlie).
          intersection(dylan),
          "\n")

    print("Only Alice has:",
          alice.difference(bob).
          difference(charlie).
          difference(dylan),
          "\n")
    print("Only Bob has:",
          bob.difference(alice).
          difference(charlie).
          difference(dylan),
          "\n")
    print("Only Charlie has:",
          charlie.difference(alice).
          difference(bob).
          difference(dylan),
          "\n")
    print("Only Dylan has:",
          dylan.difference(alice).
          difference(bob).
          difference(charlie),
          "\n")

    print("Alive is missing:", get_achievements().difference(alice))
    print("Bob is missing:", get_achievements().difference(bob))
    print("Charlie is missing:", get_achievements().difference(charlie))
    print("Dylan is missing:", get_achievements().difference(dylan))
