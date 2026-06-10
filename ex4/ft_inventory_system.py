from sys import argv


def parse_record(record: str) -> tuple[str, int]:
    kv_list: list[str] = record.split(":")
    if len(kv_list) == 2:
        key: str = kv_list[0]
        try:
            value: int = int(kv_list[1])
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
    try:
        kv: tuple[str, int] = parse_record(record)
        if not inventory.get(kv[0]):
            inventory[kv[0]] = kv[1]
        else:
            raise RuntimeError(
                f"Redundant item '{kv[0]}' - discarding"
            )
    except Exception as e:
        print(e)


def get_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
    for record in argv[1:]:
        try_append_record(record, inventory)
    return inventory


def find_min(inventory: dict[str, int]) -> tuple[str, int]:
    min_val: int = min(inventory.values())
    key: str = [k for k in inventory.keys() if inventory[k] == min_val][0]
    return (key, min_val)


def find_max(inventory: dict[str, int]) -> tuple[str, int]:
    max_val: int = max(inventory.values())
    key: str = [k for k in inventory.keys() if inventory[k] == max_val][0]
    return (key, max_val)


if __name__ == "__main__":
    inventory: dict[str, int] = get_inventory()
    count: int = sum(inventory.values())
    min_count_item: tuple[str, int] = find_min(inventory)
    max_count_item: tuple[str, int] = find_max(inventory)
    item_count: int = len(inventory)
    rate: float
    print("Got inventory:", inventory)
    print("Item list:", inventory.keys())
    print(
        "Total quantity of the",
        item_count, "items:", count
    )
    for item, value in inventory.items():
        if count:
            rate = value / count
        else:
            rate = 0.
        print(f"Item {item} represents",
              f"{rate * 100:.1f}%")
    print(f"Item most abundant: {max_count_item[0]}",
          f"with quantity {max_count_item[1]}")
    print(f"Item least abundant: {min_count_item[0]}",
          f"with quantity {min_count_item[1]}")
    inventory["magic_item"] = 1
    print("Update inventory:", inventory)
