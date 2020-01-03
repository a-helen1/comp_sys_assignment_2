
#!/user/bin/env python

# import libraries
import serial
import time
import mysql.connector
from wia import Wia

# connect to local database containing tank voilume  map
db= mysql.connector.connect(user='admin',password='admin',host='localhost',database='tank_level')

# set db cursor
c = db.cursor(buffered=True)


wia = Wia()

wia.access_token = "access_token"

# set serial port to communicate with arduino
port = "/dev/ttyACM0"

# start serial
s1 = serial.Serial(port, 9600)
s1.flushInput()
sensorHeight = 3000 #distance in mm from bottom of empty tank to sensor
while True:
        if s1.inWaiting()>0:
                inputValue=s1.readline().strip().decode("utf-8") # read string from serial
                measuredHeight = (int(inputValue)) # convert string to int
                height =sensorHeight - measuredHeight
                print height
                c.execute("select volume from levelMap where height=%s",(height,)) # query  db for tank volume
                result = c.fetchone() # return result of query
                volume = ( "{}".format(result[0])) # format query result into a string
                print volume
                wia.Event.publish(name="Level", data=volume) # push volume to wia
                time.sleep(15) # wait  to prevent flodding wia
                s1.flushInput() # clear serial input.
