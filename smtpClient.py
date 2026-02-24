from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Computer Networking is FUN!" #Message body
    endmsg = "\r\n.\r\n" # This is the CRLF

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)  # AF_INET - INTERNET , SOCK_STEAM-TCP
    clientSocket.connect((mailserver, port)) # Establishes connection with mailserver and port

    recv = clientSocket.recv(1024).decode()
    if recv[:3] != '220':
        return
        

    

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] != '250':
        return
        

    # Send MAIL FROM command and handle server response.
    mailFromCommand = 'MAIL FROM:<bobsburgers@cn.com>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    if recv2[:3] != '250':
        return
        

    # Send RCPT TO command and handle server response.
    rcptToCommand = 'RCPT TO:<sushilover@californiaroll.com>\r\n'
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    if recv3[:3] != '250':
        return
        

    # Send DATA command and handle server response.
    sendDataCommand = 'DATA\r\n'
    clientSocket.send(sendDataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    if recv4[:3] != '354':
        return
        

    # Send message data
    clientSocket.send(msg.encode())

    # Message needs to end with a '.'
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    if recv5[:3] != '250':
        return
        

    # Send QUIT command and handle server response.
    sendQuitCommand = 'QUIT\r\n'
    clientSocket.send(sendQuitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    if recv6[:3] != '221':
        return
        

    clientSocket.close()


if __name__ == '__main__':

    smtp_client(1025, '127.0.0.1')





