import sys


def handle_command(command):
    if command == "exit":
        sys.exit(0)
    else:
        sys.stdout.write(f"{command}: command not found\n")

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        # Handle Command
        handle_command(command)

if __name__ == "__main__":
    main()
