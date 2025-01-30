# Introduction

Netcat, a networking tool, facilitates reading & writing to network connections over TCP or UDP.

In this document, I will show you how I created a netcat-eqsue reverse shell listener using Python.

We will be using the following libraries:
1. Socket
2. System
3. Time

The socket library (and the others) should have been included with your install of Python.
If not, you can use the following script in your terminal to install the socket library.
    pip install socket

Btw, if you are running Linux and only have access to the terminal, you can use _nano_ or _vim_.

# Source code

    import socket, sys, time

Imports the libraries needed to create the script.

    def listen(ip, port):
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen(1)
        print("Listening on port " + str(port))
        
        conn, addr = s.accept()
        print('Connection received from ', addr)

Defining our listen function with ip and ports. We define our sockets and then bind them with ip and ports. 

Here, we create an artificial delay of 1 second.

Then, we print that we are listening on ports, concatenating the port specified.

After a connection has been made, we print as such, concatenating the address.

    while True:
        try:
            ans = conn.recv(1024).decode()
            sys.stdout.write(ans + "\n")
        except ConnectionResetError:
            print("Connection lost.")
            break

Next, we create a while loop. Using the variable name ans (short for answer), we decode the received connection so that we can display it in Python. We then take an input from the user.

    command = input("> ")
        if command.lower() == "exit":
            print("Closing connection.")
            conn.close()
            break

        conn.send((command + "\n").encode())
        time.sleep(1)

After we get the input from the user, we encode it when we send it (so that it is properly sent). We then create an artificial timeout so that the command is sent properly.

    listen("0.0.0.0",9999)

Lastly, we set up our listener.

Obviously, the IP will have to be your computer's address.

The port can be whatever you'd like. Obviously, you cannot use a port that is already in use, or you will have an error upon launching the program.

# Video example of intended functionality



# Areas of improvement

This script could be improved by taking the IP and port numbers as an input variable in the CLI. I may action this in the future.

# WARNING!

Use of a reverse shell to gain access to another computer or network without permission is ILLEGAL.

Please only use this tool in a VM or on your personal network :)
