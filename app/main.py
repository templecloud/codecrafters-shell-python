import sys


def handle_command(command):
    parts = command.split(" ")
    cmd = parts[0] if len(parts) > 0 else None
    arg1 = parts[1] if len(parts) > 1 else None

    if cmd == "exit":
        exit_code = 0 
        try:
            exit_code = int(arg1) if arg1 else 0
        except ValueError:
            exit_code = 0
        sys.exit(exit_code)
    else:
        sys.stdout.write(f"{cmd}: command not found\n")

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
