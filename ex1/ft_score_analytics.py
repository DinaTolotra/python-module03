import sys


def parse_arg(argv: list[str]) -> list[int]:
    result: list[int] = list()
    nb: int
    for arg in argv[1:]:
        try:
            nb = int(arg)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
        result += [nb]
    return result


if __name__ == "__main__":
    score_list: list[int] = parse_arg(sys.argv)
    len_score: float = len(score_list)
    print("=== Player Score Analytics ===")
    if len_score > 0:
        min_score: int = min(score_list)
        max_score: int = max(score_list)
        sum_score: int = sum(score_list)
        print("Scores processed:", score_list)
        print("Total players:", len_score)
        print("Total score:", sum_score)
        print("Average score:", sum_score / len_score)
        print("High score:", max_score)
        print("Low score:", min_score)
        print("Score range:", max_score - min_score)
    else:
        print(
            "No scores provided. Usage:",
            "python3 ft_score_analytics.py",
            "<score1> <score2> ..."
        )
