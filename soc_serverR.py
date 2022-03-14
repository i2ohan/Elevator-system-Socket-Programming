# first of all import the socket library
import socket
from elevator import Elevator
import pickle

global customers, floors, objElevator, direction

def interp(arrString):

    print(arrString)
    inString=arrString[len(arrString)-1]
    arrString.remove(arrString[len(arrString)-1])
    cmdString=inString.split("|")
    floornumbers=arrString[0]

    for i in range(0,len(cmdString)):
        print(cmdString[i])
        param, val = cmdString[i].split(":")
        if param == "CUST":
            customers=val
            print("Total Customers:" + customers)
        elif param == "FL":
            floors =val
            objElevator = Elevator(floors,floors)
            print("Total Floors:"+floors)
        elif param == "DIR":
            direction=val
            print("Direction:"+direction)

    for i in range(0,len(floornumbers)):
        print("customer #"+ str(i+1) +": on floor #" + floornumbers[i])
        objElevator.open()


# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # send a thank you message to the client.
    c.send(b'thanks')

    data=c.recv(1024)
    print(data)
    arrString = pickle.loads(data)
    interp(arrString)

    #floor_count, customer_count = data.decode("utf-8").split(',')
    #print("f:"+floor_count)
    #print("c:"+customer_count)

    #objElevator = Elevator(data.length)
    #objElevator.open()


#   if data == b'1':
#       print("level1")
#
#       Elevator.open()
#  else:
#       print("level" + str(data))
#       c.close()
#       break

    # Close the connection with the client
    #c.close()

s.close()