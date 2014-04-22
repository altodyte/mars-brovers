import time
import string
import socket
from flask import Flask, request
    
#s = '$,R,10,100,G,500,1000,B,90,270,V,0,0,W,0,0,X,0,55,Y,0,0,Z,10,0,S,19,29,122\r'

UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("", UDP_PORT)) 
app = Flask(__name__)

#app.config['DEBUG'] = True

@app.route('/Jefferson')
def jefferson_send():
    data, addr = sock.recvfrom(1024)
    print "received message:", data
    coordinates = getOurPosition(data)
    Waypoints = getWayPoints(data)
    '''print Waypoints
    x = coordinates[0]
    y = coordinates[1]'''
    print Waypoints
    for i in range(len(Waypoints)):
        WaypointsCheck = checkWaypoints(Waypoints[i],coordinates)
        if WaypointsCheck == 1:
            cleared = Waypoints.pop(i)

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

def checkWaypoints(Waypoint,Coordinates):
        x = coordinates[0]
        y = coordinates[1]
        if x >= Waypoints[0] - 5 and Waypoints[0] + 5:
            if y >= Waypoints[1] - 5 and Waypoints[1] + 5:
                print "X passed, Y passed"
                return 1
            else:
                "X passed, Y faild"
                return 0
        elif y >= Waypoints[1] - 5 and Waypoints[1] +5:
            print "X failed, Y Passed"
        else:
            "X failed, Y failed"
            return 0

#http://<ip_address>:<Port>/Jefferson


if __name__ == '__main__':
    app.run(host='0.0.0.0')
