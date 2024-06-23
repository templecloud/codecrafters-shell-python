import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    
    # Handle Command
    sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
