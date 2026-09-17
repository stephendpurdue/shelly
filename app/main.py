import sys
import shutil


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush() # Forces buffered text to the terminal

        try:
            cmd = input()
        except EOFError:
            break
    
        if cmd == "exit":
            break
        elif cmd.startswith("echo "):
            print(cmd[5:])

        elif cmd.startswith("type "):
            target = cmd[5:]
            if target in ["type", "echo", "exit"]:
                print(f"{target} is a shell builtin")
            elif path := shutil.which(target):
                print(f"{target} is {path}")
            else:
                print(f"{target}: not found")

        elif path := shutil.which(cmd):
            print(f"{cmd} is {path}")

        else:
            print(f"{cmd}: not found")


if __name__ == "__main__":
    main()
