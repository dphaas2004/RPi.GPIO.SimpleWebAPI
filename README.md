# RPi.GPIO.SimpleWebAPI
## What is this repositoty?
I wrote this API for my son.  After doing some searching I was not able to find a simple way to control the IO on a raspberry pi quickly and visually using a GUI.
Since hes young and learning I wanted a way for him to quickly be able to validate his circuits were working properly without the need to understand and know how to write lots of code.
So thats what I've set out to do.

## Who is this repository for?
As I mentioned I wrote this for my son.  He is nine.  So, in my mind this repository is for anyone new to coding or the raspberry pi or both that its looking for simple ways to validate functionality or mess around with the IO on the board.
I myself am not a professional programmer and im sure there are many thing that could be improved in this code base and for that reason i would not recommend this code for production use.  Its just for fun!

## What is the API
The API itself consists of two pieces of code.  A javascript library RPiGPIO.js and a python script GPIO.py.  
The Javascript library provide a collection of functions to manipulate the IO.  The functions are all contained in a parent object "Rpi" and a sub object "GPIO".  Further details can be found in the API section below.
The python script allows the web client to interact with the server and execute the commands on the IO.  

## Javascript API

## Python Stuff
There are two main Python libraries for controlling the Raspberry Pi that im familiar with.  RPi.GPIO and GPIOZERO.  I have chosen to use the former of these two specifically due to GPIOZERO's automated cleanup at the end of the script.

## Other things
I Really like pinout.xyz's graphic of the raspberry pi.
I think it makes it very easy to explain the GPIO layout and the pin locations.  For this reason I have provided a Server.sh script to initiate a Simple Python web server and an index.html page that renders this graphic and overlays the API.
to run the web server just run `bash Server.sh` or `./Server.sh`
the webpage is available on prort 8000.  To access open a web browser and enter the IP adderss of the device with :8000 appended to it

#This Repo is a work in progress and may not function as expected


