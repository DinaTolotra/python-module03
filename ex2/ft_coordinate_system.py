import math


def get_coord_input() -> list[str]:
    line: str

    line = input("Enter new coordinates " +
                 "as floats in format " +
                 "'x,y,z': ")
    return line.split(",")


def convert_list_content(lst: list[str]) -> list[float]:
    res: list[float]

    res = []
    for i in range(len(lst)):
        try:
            res.append(float(lst[i]))
        except ValueError as e:
            print("Error on parameter",
                  f"'{lst[i]}': {e}")
            res.clear()
    return res


def get_player_pos() -> tuple[float, float, float]:
    coord: tuple[float, float, float]
    coord_str: list[str]

    coord = ()
    while not coord:
        coord_str = get_coord_input()
        if len(coord_str) == 3:
            coord = tuple[float](
                convert_list_content(coord_str)
            )
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
          f"{get_dist(coord1, coord2):.4f}")
