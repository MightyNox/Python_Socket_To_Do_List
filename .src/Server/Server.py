import socket
import json


def show_requests():
    print("Showing list of requests")
    with open("requests_list.json") as json_data:
        data = json.load(json_data)
    return data


def add_request(request_desc, reques_priority):
    print("Adding request")
    with open("requests_list.json") as json_data:
        data = json.load(json_data)

    unique_ID = data["unique_id"]
    self = ""
    seq = ("request", str(unique_ID))
    name = self.join(seq)

    data[name] = {}
    data[name] = {"id": unique_ID, "desc": request_desc, "priority": reques_priority}
    data["unique_id"] = unique_ID + 1

    with open("requests_list.json", 'w') as json_data:
        json.dump(data, json_data)

    self = ""
    seq = ("Request added with ID: ", str(unique_ID))
    return self.join(seq)


def delete_request(request_id):
    print("Deleting request")
    with open("requests_list.json") as json_data:
        data = json.load(json_data)

    self = ""
    seq = ("request", str(request_id))
    name = self.join(seq)

    try:
        del data[name]
    except KeyError:
        print("Key doesn't exist")
        return "Wrong ID!"

    with open("requests_list.json", 'w') as json_data:
        json.dump(data, json_data)

    return "Request deleted"


def show_request_by_priority():
    print("Showing list of requests with selected priority")
    with open("requests_list.json") as json_data:
        data = json.load(json_data)
    return data


def switch(argument, request_desc, request_priority, request_i_d):
    if argument == 1:
        return show_requests()
    elif argument == 2:
        return add_request(request_desc, request_priority)
    elif argument == 3:
        return delete_request(request_i_d)
    elif argument == 4:
        return show_request_by_priority()
    else:
        return "ERROR"


def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.getprotobyname('tcp'))
    serv.bind(("localhost", 8888))
    serv.listen(1)
    return serv


def main():
    while 1:
        client, addr = server().accept()
        print("Connected with", addr)

        clientMsg = client.recv(64).decode()

        print("Client msg: ", clientMsg)
        clientMsg = clientMsg.split(".")

        i = 0
        functionNumber = -1
        requestDesc = ""
        requestPriority = -1
        requestID = -1
        for x in clientMsg:
            if i == 0:
                functionNumber = int(x)
            if i == 1:
                requestDesc = x
            if i == 2:
                requestPriority = int(x)
            if i == 3:
                requestID = int(x)
            i += 1

        client.send(str(switch(functionNumber, requestDesc, requestPriority, requestID)).encode())
        client.close()
        print()


if __name__ == '__main__':
    main()
