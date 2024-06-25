import sys


def handle_command(command):
    cmd_tokens = command.split(" ")
    cmd = cmd_tokens[0] if len(cmd_tokens) > 0 else None

    if cmd == "exit":
        arg1 = cmd_tokens[1] if len(cmd_tokens) > 1 else None
        exit_code = 0 
        try:
            exit_code = int(arg1) if arg1 else 0
        except ValueError:
            exit_code = 0
        sys.exit(exit_code)
    elif cmd == "echo":
        to_echo = command[len(cmd) + 1:]
        sys.stdout.write(to_echo + "\n")

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
