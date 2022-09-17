################need to insert in encoder#############################
lf ='11111111111111111111'
SENDING = '1'+ send_array + lf
###############################arduino_setup#######################
COM_PORT = 'COM8'
BAUD_RATES = 115200

ser = serial.Serial(COM_PORT, BAUD_RATES)   #Create Serial port object called arduinoSerialData
ser.setDTR(1)
time.sleep(0.25)
ser.setDTR(0)
print (ser.readline())                      #read the serial data and print it as line
print ("Press enter to send file")
a = len(SENDING)
print(a)
#######################MAIN#####################################
#start = input()
                         
while input():                           #infinite loop
    #print ("Start Sending")                  #prints the data for confirmation
    for i in range(a):
        
        if (SENDING[i] == '1'):                 #if the entered data is 1 
            ser.write(b'1')                     #send 1 to arduino
            print ("LED ON")
                 
        else:                                   #if the entered data is 0
            ser.write(b'0')                      #send 0 to arduino 
            print ("LED OFF")
        print("now sending number",i,)

        time.sleep(.003)
    break
