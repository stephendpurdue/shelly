import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        # Commands 
        if command == "exit".lower():
            break
        if command.startswith("echo "):
            print(command[5:])
        else:
            print(f"{command}: command not found")

        


if __name__ == "__main__":
    main()
