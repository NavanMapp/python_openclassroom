Instructions

It's the year 2000. You're working for a mobile phone company and have been tasked with modeling out the software for a cutting-edge phone that will have a built-in camera: a camera phone.

Create a class called Camera and a class called MobilePhone that will be the base classes of a derived class called CameraPhone. The CameraPhone class should be initialized with the memory attribute and should have a take_picture() method that prints out the message, Say cheese!.

The steps are as follows:

Create a Camera class with a take_picture() method that prints the message, "Say cheese!".

Create a MobilePhone class that will be initialized with a memory attribute.

Create a CameraPhone class that inherits from both the MobilePhone and Camera classes.

At the bottom of the script we have initialized an instance of the CameraPhone class and passed it the value "200KB". Then we call the take_picture() method and also print out the memory attribute. Run the script with python main.py command and we should have an output that looks like this:

Say cheese!

200KB