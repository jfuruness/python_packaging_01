from pathlib import Path

from .speakers import Justin
# from justin_furuness.speakers import Justin

def main():
    Justin().print_name()
    # with open("names.txt") as f:
    with (Path(__file__).parent / "names.txt").open() as f:
        print(f.read())

if __name__ == "__main__":
    main()