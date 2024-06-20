import sys


def main():
    busybox = [
        "echo"
    ]

    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()

        # Exit the shell
        if command == "exit" or command == "exit 0":
            break

        if command.split(" ")[0] not in busybox:
            sys.stdout.write(f'{command}: command not found\n')
            continue

        if command.split(" ")[0] == "echo":
            command = command.split(" ")
            sys.stdout.write(f"{command[1:]}\n")
            continue


if __name__ == "__main__":
    main()
