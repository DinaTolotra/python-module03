from sys import argv


def parse_record(record: str) -> tuple[str, int]:
    kv_list: list[str]
    key: str
    value: int

    kv_list = record.split(":")
    if len(kv_list) == 2:
        key = kv_list[0]
        try:
            value = int(kv_list[1])
        except ValueError as e:
            raise ValueError(
                f"Quantity error for '{key}': {e}"
            )
        return (key, value)
    else:
        raise ValueError(
            f"Error - invalid parameter '{record}'"
        )


def try_append_record(record: str, inventory: dict[str, int]) -> None:
    kv: tuple[str, int]

    try:
        kv = parse_record(record)
        if not inventory.get(kv[0]):
            inventory[kv[0]] = kv[1]
        else:
            raise RuntimeError(
                f"Redundant item '{kv[0]}' - discarding"
            )
    except Exception as e:
        print(e)


def get_inventory() -> dict[str, int]:
    inventory: dict[str, int]

    inventory = {}
    for record in argv[1:]:
        try_append_record(record, inventory)
    return inventory


def find_min(inventory: dict[str, int]) -> tuple[str, int]:
    min_val: int
    key: str

    min_val = min(inventory.values())
    key = [k for k in inventory.keys() if inventory[k] == min_val][0]
    return (key, min_val)


def find_max(inventory: dict[str, int]) -> tuple[str, int]:
    max_val: int
    key: str

    max_val = max(inventory.values())
    key = [k for k in inventory.keys() if inventory[k] == max_val][0]
    return (key, max_val)


if __name__ == "__main__":
    inventory: dict[str, int]
    min_count_item: tuple[str, int]
    max_count_item: tuple[str, int]
    count: int

    inventory = get_inventory()
    count = sum(inventory.values())
    min_count_item = find_min(inventory)
    max_count_item = find_max(inventory)
    print("Got inventory:", inventory)
    print("Item list:", inventory.keys())
    print("Total quantity of the",
          len(inventory.keys()),
          "items:",
          count
          )
    for item, value in inventory.items():
        print(f"Item {item} represents",
              f"{(value / count) * 100:.1f}%")
    print(f"Item most abundant: {max_count_item[0]}",
          f"with quantity {max_count_item[1]}")
    print(f"Item least abundant: {min_count_item[0]}",
          f"with quantity {min_count_item[1]}")
    inventory["magic_item"] = 1
    print("Update inventory:", inventory)
