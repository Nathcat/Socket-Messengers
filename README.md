# Socket-Messengers

The Python socket module creates a pipeline for messages, it is a streaming based service, this means that large messages may lose a lot
of data.

This script "SocketMessengers.py" makes sure that large messages are fully sent and recieved by using the struct module,
data is prefixed with the length of the total data being sent, and the server will continue to recieve data until
it has recieved the amount of data specified by the prefix.

 - Nathcat :P
