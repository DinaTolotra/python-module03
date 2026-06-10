import sys


def parse_arg(arg: list[str]) -> list[int]:
    result: list[int] = list()
    nb: int

    for i in range(1, len(arg)):
        try:
            nb = int(arg[i])
        except ValueError:
            print(f"Invalid parameter: '{arg[i]}'")
        result += [nb]
    return result


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_list: list[int] = parse_arg(sys.argv)
    if len(score_list) > 0:
        print("Scores processed:", score_list)
        print("Total players:", len(score_list))
        print("Total score:", sum(score_list))
        print("Average score:",
              sum(score_list) / len(score_list))
        print("High score:", max(score_list))
        print("Low score:", min(score_list))
        print("Score range:", max(score_list) - min(score_list))
    else:
        print(
            "No scores provided. Usage:",
            "python3 ft_score_analytics.py",
            "<score1> <score2> ..."
        )
