from typing import Generator
import random


def gen_event(n: int) -> Generator[tuple[str, str], None, None]:
    action_list: list[str] = [
        "run", "eat", "sleep", "grab",
        "move", "climb", "swim", "release",
    ]
    name_list: list[str] = [
        "alice", "bob", "charlie", "dylan",
    ]
    for i in range(n):
        yield (random.choice(name_list),
               random.choice(action_list))


def consume_event(
    event_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    initial_len: int = len(event_list)
    rand_index: int
    for i in range(len(event_list)):
        rand_index = random.randrange(
            0, initial_len - i
        )
        yield event_list.pop(rand_index)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    event_count: int = 0
    for (name, action) in gen_event(1000):
        print(f"Event: {event_count}:",
              f"Player {name} did",
              f"actio {action}")
        event_count += 1
    event_list: list[tuple[str, str]] = [
        event for event in gen_event(10)
    ]
    print("Built list of 10 events:", event_list)
    for event in consume_event(event_list):
        print("Got event from list:", event)
        print("Remains in list:", event_list)
