if __name__ == '__main__':
    N = int(input())
    command_list = []
    for _ in range(N):
        command, *line = input().split()
        positions = list(map(int, line))
        if command == "insert":
            command_list.insert(positions[0], positions[1])
        elif command == "append":
            command_list.append(positions[0])
        elif command == "print":
            print(command_list)
        elif command == "remove":
            command_list.remove(positions[0])
        elif command == "sort":
            command_list.sort()
        elif command == "pop":
            command_list.pop()
        else:
            command_list.reverse()
