import math


def get_coord_input() -> tuple[str, str, str] | None:
    res: tuple[str, str, str] | None = None
    input_list: list[str] | None = None
    input_prompt: str = (
        "Enter new coordinates "
        "as floats in format "
        "'x,y,z': "
    )
    try:
        line: str = input(input_prompt)
        input_list: list[str] = line.split(",")
    except BaseException:
        pass
    if input_list and len(input_list) == 3:
        res = (input_list[0], input_list[1], input_list[2])
    return res


def try_convert_str_to_float(s: str) -> float:
    try:
        return float(s)
    except ValueError as error:
        raise ValueError(
            f"Error on parameter '{s}': "
            + str(error)
        )


def convert_list_content(coord_str: tuple[str, str, str]) -> tuple[float]:
    try:
        return (
            try_convert_str_to_float(coord_str[0]),
            try_convert_str_to_float(coord_str[1]),
            try_convert_str_to_float(coord_str[2])
        )
    except ValueError as error:
        print(error)


def get_player_pos() -> tuple[float, float, float] | None:
    coord: tuple[float, float, float] | None = None
    coord_str: list[str]
    while not coord:
        coord_str = get_coord_input()
        if coord_str:
            coord = convert_list_content(coord_str)
        else:
            print("Invalid syntax")
    return coord


def get_dist(
        p1: tuple[float, float, float],
        p2: tuple[float, float, float]
        ) -> float:
    return math.sqrt(
        (p2[0] - p1[0])**2 +
        (p2[1] - p1[1])**2 +
        (p2[2] - p1[2])**2
    )


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    coord1: tuple[float, float, float]
    coord2: tuple[float, float, float]

    print("Get a first set of coordinates")
    coord1 = get_player_pos()
    print("Got a first tuple:", coord1)
    print("It includes:",
          f"X={coord1[0]},",
          f"Y={coord1[1]},",
          f"Z={coord1[2]}")
    print("Distance to center:",
          f"{get_dist(coord1, (0, 0, 0)):.4f}")

    print("\nGet a second set of coordinates")
    coord2 = get_player_pos()
    print("Distance between the 2 sets of coordinates:",
          f"{round(get_dist(coord1, coord2), 4)}")
