##import serial library
import serial

##Boolean that will represent if arduino is connected
connected = False

##open serial port with the arduino
ser = serial.Serial ("COM3",9600)

##loop until arduino says it is ready
while not connected:
  serin = ser.read()
  connected = True

## Tell arduino to blink
ser.write("1")

##Wait until arduino says it finesh blinking
while ser.read()=='1':
  ser.read()

##Close the port
ser.close()
