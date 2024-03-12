#!/usr/bin/env python3
#Script to initialize, get and set GPIO pins for RPi
import sys
import cgi
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
args = cgi.FieldStorage()
print('Content-Type: text/html\n\n')
if "Action" not in args:
    print(f'Error. Please provide an Action for Pin#{Pin}')
    exit
GPIO.setmode(GPIO.BCM)
Action = args['Action'].value #Get Action 
if Action == "Mode":
    if "Value" in args:
       ModeVal = args['Value'].value
       if ModeVal != 'BOARD' or 'BCM':
           print('Error.  Invalid Mode')
           sys.exit()
       GPIO.setmode(GPIO.BCM if ModeVal == 'BCM' else GPIO.BOARD)
    else:
        Mode = GPIO.getmode()
    Mode = 'BCM' if Mode == 11 else 'BOARD'
    print(Mode)
    sys.exit()
if "Pin" not in args:
    print('Error. Please provide a Pin #')
    sys.exit()
Pin = args['Pin'].value #Get Pin #   
Pin=int(Pin)
if Action == "Get":
    #print(f'Getting Pin#{Pin} value...')
    GPIO.setup(Pin, GPIO.OUT)
    Val=GPIO.input(Pin)
    #print(f'The Value of Pin#{Pin} is {Val}')
    print(Val)
    sys.exit()
elif Action == "Set":
    if "Value" not in args:
        print(f'Error. Value not set for Pin#{Pin}')
        sys.exit()
    Value = args['Value'].value #Get Value
    Value = int(Value)
    print(f'Setting pin#{Pin} to {Value}....')
    GPIO.setup(Pin, GPIO.OUT, initial=Value)
    sys.exit()
else:
    GPIO.cleanup()
    print(f'Error. Unknown Action {Action} Please Try again')

'''
GPIO.setup(17, GPIO.OUT) 
GPIO.output(17, True) 
sleep(2) 
GPIO.output(17, False)
'''