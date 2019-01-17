import socket
import ast


def bubble_sort(arr):
    array = []
    for x in arr:
        array.append(x[2])
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
                temp = array[i]
                temp1 = arr[i]
                array[i] = array[i + 1]
                arr[i] = arr[i + 1]
                array[i + 1] = temp
                arr[i + 1] = temp1


def send_packet(data, function_number):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.getprotobyname('tcp'))
    s.connect(("localhost", 8888))
    s.send(str(data).encode())

    message = s.recv(1024)
    s.close()

    if function_number == 1:
        data = ast.literal_eval(message.decode())
        print("ID", end=" | ")
        print("DESC", end=" | ")
        print("PRIORITY")

        i = 0
        for x in data:
            if i == 0:
                i += 1
                continue
            print(data[x]["id"], end=" | ")
            print(data[x]["desc"], end=" | ")
            print(data[x]["priority"])
    elif function_number == 4:
        data = ast.literal_eval(message.decode())
        print("ID", end=" | ")
        print("DESC", end=" | ")
        print("PRIORITY")

        table = []
        i = 0
        for x in data:
            if i == 0:
                i += 1
                continue
            temptable = [data[x]["id"], data[x]["desc"], data[x]["priority"]]
            table.append(temptable)
        bubble_sort(table)
        i = 0
        for x in table:
            print(table[i][0], end=" | ")
            print(table[i][1], end=" | ")
            print(table[i][2])
            i += 1

    else:
        print(message.decode())


def main():
    function_number = -1
    while function_number != 0:
        request_description = ""
        request_priority = -1
        request_id = -1
        print("0 - Exit")
        print("1 - Show requests")
        print("2 - Add request")
        print("3 - Delete request")
        print("4 - Show requests with priority")
        function_number = input("Select option: ")
        if function_number.isnumeric():
            function_number = int(function_number)
        else:
            print("Option must be a number!")
            print()
            continue
        if function_number < 0 or function_number > 4:
            print("Incorrect option!")
            print()
            continue
        if function_number == 2:
            request_description = input("Type description of the request: ")
            request_priority = input("Type priority of the request: ")
            if not request_priority.isnumeric():
                print("Priority must be a number!")
                print()
                continue
        if function_number == 3:
            request_id = input("Type ID to delete: ")
            if not request_id.isnumeric():
                print("ID must be a number!")
                print()
                continue
        if function_number != 0:
            self = "."
            seq = (str(function_number), request_description, str(request_priority), str(request_id))
            try:
                send_packet(self.join(seq), function_number)
            except ConnectionRefusedError:
                print("Unable to connect to the server")
            print()


if __name__ == '__main__':
    main()
