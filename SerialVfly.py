import time
import serial
from time import sleep
ser = 0


def init_serialport_linux(num):     # initialization function running on linux
        # COMNUM = 1 Enter Your COM Port Number Here.
    global ser          # Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 9600
    # ser.port = COMNUM - 1   #COM Port Name Start from 0
    if num in range(4):
        ser.port = '/dev/ttyUSB%d' % num
    else:
        print "unacceptable port number please give a right one"

        # Specify the TimeOut in seconds, so that SerialPort
        # Doesn't hangs
    ser.timeout = 4
    ser.open()          # Opens SerialPort

    # print port open or closed
    if ser.isOpen():
        print 'Initialized port: ' + ser.portstr
        print 'Open: ' + ser.portstr
        return None
# Function Ends Here


def init_serialport_windows(num):  # initialization function running on windows

    # COMNUM = num  # Enter Your COM Port Number Here.
    global ser          # Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 9600

    if num in range(4):
        ser.port = 'COM%d' % num
    else:
        print "unacceptable port number please give a right one"

        # Specify the TimeOut in seconds, so that SerialPort
        # Doesn't hangs
    ser.timeout = 4
    ser.open()          # Opens SerialPort

    # print port open or closed
    if ser.isOpen():
        print 'Initialized port: ' + ser.portstr
        print 'Open: ' + ser.portstr
        return None


def close_serialport():   # Closes SerialPort
    ser.close()
    if ser.isClose():
        print 'Closed: ' + ser.portstr
    return None


def read_port():        # Reads the ports whisper until the \n character
    global data = ser.readline()
    print "the data I received is " + data
    return data


def write_port(info):   # Whispers the information
    ser.write(info)
    print "I tried to send that data via " + ser.name
    return None


# Call the Serial Initilization Function, Main Program Starts from here
# init_serialport(num)

# Ctrl+C to Close Python Window


def collector():    # Collecting datas from serialport
    xbee_data = read_port()
    xbee_data_string = xbee_data.split(",")
    print xbee_data
    if xbee_data_string[0] == "AAA" && xbee_data_string[-1] == "ZZZ":
        coordinat = xbee_data_string[1]
        velocity = xbee_data_string[2]
        temperature = xbee_data_string[3]
        pressure = xbee_data_string[4]

    elif xbee_data_string[0]=="BBB":
        function = xbee_data_string[1]

    else:
        print "invalid value"

