##########################arduino_setup#######################
COM_PORT = 'COM4'
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES) #Create Serial port object called arduinoSerialData
#ser.bytesize = 8  
############################RECEIVE#####################################
#start = input()                   #infinite loop                           
code = '11111111111111111111'
stop = code.encode()
start = 0
ser.flush()

while(ser.inWaiting() == 0):
    time.sleep(0.05)
print ("Start receiving")          #prints the data for confirmation
time.sleep(1)
while not start:
    ser.flush()
    start_bits = ser.read()
    if start_bits == b'1':
        RECEIVE = ser.read_until(stop, None).decode()
        print(RECEIVE)
        start = True
    else:
        start = False
