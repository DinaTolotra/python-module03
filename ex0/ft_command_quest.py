import sys

if __name__ == "__main__":
    index: int = 1
    argc: int = len(sys.argv)
    prog_name: str = sys.argv[0]
    argv: list[str] = sys.argv[1:]
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    if argc > 1:
        print("Arguments received:", argc - 1)
        for arg in argv:
            print(f"Argument {index}: {arg}")
            index += 1
    else:
        print("No arguments provided!")
    print("Total arguments:", argc)
