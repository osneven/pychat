# pychat
A "secure" multi-user encrypted chat server and client written in python.
**WARNING: This is a hobby project and should only be used in educational circumstances!**

### Dependecies
* [python 3.5](python.org/download/releases)
* [cryptography](cryptography.io/en/lastest)

### Syntax
*pychat* [**COMMAND**] [**ADDRESS**] [**PORT**] [**PASSWORD**] <**NICKNAME**>
* **COMMAND** Either 'server' or 'client'. Server will setup a server ready for connections, client will connect to a server.
* **ADDRESS** The address of the server.
* **PORT** The listening port of the server.
* **PASSWORD** The encryption password of the server.
* **NICKNAME** The nick name to connect with, only used as a client.

### Example usage
*Starting a server:*
```
./pychat server 127.0.0.1 1234 password 
```
This starts a server on the IP address of **127.0.0.1** listening on port **1234** with an encryption password of **password**.

*Connecting with a client:*
```
./pychat client 127.0.0.1 1234 password Linus
```
This connects to a server with an IP address of **127.0.0.1** listening on port **1234** with an encryption password of **password** as the user **Linus**.

### Encryption
Pychat uses the fernet symetric key encryption developed by [cryptography](cryptography.io/en/lastest). As taken from their description: *Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography.*

Open connection, if the password is wrong, the client will get the message of *server closed*, otherwise if the passwords match, every user inside the server is free to chat.
