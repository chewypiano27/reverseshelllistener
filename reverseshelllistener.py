import socket, sys, time

def listen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    print("Listening on port " + str(port))

    conn, addr = s.accept()
    print('Connection received from ', addr)

    while True:
        try:
            ans = conn.recv(1024).decode()
            sys.stdout.write(ans + "\n")
        except ConnectionResetError:
            print("Connection lost.")
            break

        command = input("> ")
        if command.lower() == "exit":
            print("Closing connection.")
            conn.close()
            break

        conn.send((command + "\n").encode())
        time.sleep(1)

listen("0.0.0.0", 9999)
