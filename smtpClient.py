from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Computer Networking is FUN!" #Message body
    endmsg = "\r\n.\r\n" # This is the CRLF

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)  # AF_INET - INTERNET , SOCK_STEAM-TCP
    clientSocket.connect((mailserver, port)) # Establishes connection with mailserver and port

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':

    

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        pass

    # Send MAIL FROM command and handle server response.
    mailFromCommand = 'MAIL FROM:<bobsburgers@cn.com>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    print(recv2)
    if recv2[:3] != '250':
        pass

    # Send RCPT TO command and handle server response.
    rcptToCommand = 'RCPT TO:<sushilover@californiaroll.com>\r\n'
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    print(recv3)
    if recv3[:3] != '250':
        pass

    # Send DATA command and handle server response.
    sendDataCommand = 'DATA\r\n'
    clientSocket.send(sendDataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    print(recv4)
    if recv4[:3] != '354':
        pass

    # Send message data
    clientSocket.send(msg.encode())

    # Message needs to end with a '.'
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    print(recv5)
    if recv5[:3] != '250':
        pass

    # Send QUIT command and handle server response.
    sendQuitCommand = 'QUIT\r\n'
    clientSocket.send(sendQuitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    print(recv6)
    if recv6[:3] != '221':
        pass

    clientSocket.close()


if __name__ == '__main__':

    smtp_client(1025, '127.0.0.1')

