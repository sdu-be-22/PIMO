import threading
import socket
import argparse
import os
import sys
import tkinter as tk

class Send(threading.Thread):

    # Listens for user input from command line

    # sock the connect sock object
    #name (str) : The username provided by the user

    def __init__(self, sock, name):

        super().__init__()
        self.sock = sock
        self.name = name

    def run(self):

        while True:
            print('{}: '.format(self.name), end= '')
            sys.stdout.flush()
            message = sys.stdin.readline()[:-1]

            if message == "QUIT":
                self.sock.sendall('Server: {} has left the chat.'.format(self.name).encode('ascii'))
                break

            else:
                self.sock.sendall('{}: {}'.format(self.name, message).encode('ascii'))
                print('\nQuitting...')
                self.sock.close()
                os.exit(0)

class Receive(threading.Thread):

    def __init__(self, sock, name):

        super().__init__()
        self.sock = sock
        self.name = name
        self.messages = None

    def run(self):

        while True:
            message = self.sock.recv(1024).decode('ascii')

            if message:
                if self.messages:
                    self.messages.insert(tk.END, message)
                    print('\r{}\n{}: '.format(message, self.name), end= '')

                else:
                    print('\r{}\n{}: '.format(message, self.name), end='')

            else:
                print('\n No. We have lost connection')
                print('\nQuitting...')
                self.sock.close()
                os.exit(0)

class Client:

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.name = None
        self.message = None

    def start(self):

        print('Trying to connect to {}:{}...'.format(self.host, self.port))

        self.sock.connect((self.host, self.port))
        print('Successfully connected to {}:{}'.format(self.host,self.port))

        print()

        self.name = input('Your name: ')

        print()

        print('Welcome, {}! Getting ready to send and recieve messages...'.format(self.name))

        send = Send(self.sock,self.name)

        receive = Receive(self.sock, self.name)

        send.start()
        receive.start()

        self.sock.sendall('Server: {} has joined the chat. say whatsup!'.format(self.name).encode('ascii'))
        print("\rReady! Leave the chatroom anytime by typing 'QUIT'\n")
        print('{}:'.format(self.name),end= '')
        return receive

    def send(self,textInput):
        message = textInput.get()
        textInput.delete(0,tk.END)
        self.messages.insert(tk.END, '{}: {}'.format(self.name, message))

        if message == "QUIT":
            self.sock.sendall('Server: {} has left the chat'.format(self.name).encode('ascii'))

            print('\nQuitting...')
            self.sock.close()
            os.exit(0)

        else:
            self.sock.sendall('{}: {}'.format(self.name,message).encode('ascii'))




def main(host,port):
    client = Client(host,port)
    receive = client.start()

    window = tk.Tk()
    window.title("ChatForFriends")

    fromMessage = tk.Frame(master=window)
    scrollBar = tk.Scrollbar(master=fromMessage)
    messages = tk.Listbox(master = fromMessage, yscrollcommand= scrollBar.set)
    scrollBar.pack(side=tk.RIGHT,fill=tk.Y, expand= False)
    messages.pack(side=tk.LEFT,fill=tk.BOTH, expand= True)

    client.messages = messages
    receive.messages = messages

    fromMessage.grid(row=0,column=0,columnspan=2,sticky="nsew")
    fromEntry = tk.Frame(master=window)
    textInput = tk.Entry(master=fromEntry)

    textInput.pack(fill = tk.BOTH, expand=True)
    textInput.bind("<Return>", lambda x: client.send(textInput))

    btnSend = tk.Button(master= window,text='Send', command=lambda: client.send(textInput))
    fromEntry.grid(row=1, column=0,padx=10,sticky="ew")
    btnSend.grid(row=1, column=1,padx=10,sticky="ew")

    window.rowconfigure(0, minsize=500,weight=1)
    window.rowconfigure(1,minsize=50,weight=0)
    window.columnconfigure(0,minsize=500,weight=1)
    window.columnconfigure(1,minsize=200,weight=0)
    window.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chatroom Server")
    parser.add_argument('host',help='Interface the server listens at')
    parser.add_argument('-p',metavar='PORT',type=int,default=1060, help='TCP port(default 1060')

    args = parser.parse_args()

    main(args.host, args.p)


