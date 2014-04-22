import time
import string
import socket
from flask import Flask, request

#s = '$,R,10,100,G,500,1000,B,90,270,V,0,0,W,0,0,X,0,55,Y,0,0,Z,10,0,S,19,29,122\r'

UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind(("", UDP_PORT))
app = Flask(__name__)

@app.route('/Jefferson')
def jefferson_send():
    data, addr = sock.recvfrom(1024)
    print "received message:", data

    coordinates = getOurPosition(data)
    Waypoints = getWayPoints(data)
    
    x = coordinates[0]
    y = coordinates[1]

    #Calibration range for coordinates
    variablex = 5
    variabley = 5
    
    if x >= Waypoints[0][0] - variablex and Waypoints[0][0] + variablex:
        if y >= Waypoints[0][1] - variabley and Waypoints[0][1] + variabley:
            print "X passed, Y passed"
            popped = Waypoints.pop(0)
            print popped
            return popped
        else:
            print "X passed, Y faild"
            return WaypointCount[0]
    elif y >= Waypoints[i][1] - variabley and Waypoints[i][1] + variabley:
        print "X failed, Y Passed"
        return WaypointCount[0]
    else:
        print "X failed, Y failed"
        return WaypointCount[0]

#Data Parsing
def getSymbols(data):
	syms = [];
	for c in string.letters:
		if c in data: syms.append(c)
	return syms

def parseString(data,target):
	d = data[string.find(data,target)+2:].split(',')
	p = (int(d[0]),int(d[1]))
	return p

def getWayPoints(data):
	sym = [i for i in getSymbols(data) if i >= 'T']
	way = sorted(parseString(data,s) for s in sym)
	return way

def getOurPosition(data):
	name = 'G'
	return parseString(data,name)

#http://<ip_address>:<Port>/Jefferson

if __name__ == '__main__':
    app.run(host='0.0.0.0')
