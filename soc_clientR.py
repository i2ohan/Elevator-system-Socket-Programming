# Import socket module
import socket
import pickle


# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))
# receive data from the server
print(s.recv(1024))

# send data to server
customer_floor = []
sendString = []
customer_count = str(input("How many customers are in the building?: "))
floor_count = str(input("How many floors does the building have?: "))
elevatorDirection = str(input("Press 1 for UP and 0 for Down:"))
for i in range(0,int(customer_count)):
    cust=i+1
    floor = str(input("Customer #" + str(cust) + " which floor do you want to go?"))
    customer_floor.append(floor)
print(customer_floor)
sendString.append(customer_floor)
sendString.append("CUST:"+customer_count+"|"+"FL:"+floor_count+"|"+"DIR:"+elevatorDirection)
print(sendString)
s.send(pickle.dumps(sendString))



# close the connection
s.close()

