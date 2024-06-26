import os
import sys
import subprocess

builtins = { "exit", "echo", "type" }

def has_command(name) -> bool:
    return get_binary_path(name) is not None


def get_binary_path(name) ->  str:
    paths = os.environ.get('PATH').split(":")
    for path in paths:
        p = path.strip()
        if os.path.isdir(p):
            files = os.listdir(p)
            for file in files:
                if file == name:
                    return path + "/" + name
    return None


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
        return
    elif cmd == "type":
        arg1 = cmd_tokens[1] if len(cmd_tokens) > 1 else None
        if arg1 in builtins:
            sys.stdout.write(f"{arg1} is a shell builtin\n")
            return
        else:
            cmd = get_binary_path(arg1)
            if cmd:
                sys.stdout.write(f"{arg1} is {cmd}\n")
                return
        if arg1:
            sys.stdout.write(f"{arg1}: not found\n")
            return
    else:
        arg1 = cmd_tokens[1] if len(cmd_tokens) > 1 else None
        if has_command(cmd):
            try:
                subprocess.run([cmd] + cmd_tokens[1:])
            except FileNotFoundError:
                sys.stdout.write(f"{cmd}: command not found\n")
            return
        else:
            sys.stdout.write(f"{cmd}: command not found\n")
            return


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
