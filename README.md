# simple_reverseshell
A very basic and simple reverse shell written in Python3. Made in ~30 minutes.
It works like this:
The person wanting reverse shell access needs to start the server script. Then the one giving reverse shell access should run the client script. It is very basic, so you can't really use it as malware. E.g., you can't use the cd command. But if you want to use this as malware, you can for example change the client script with deleting the parameters and just assign the variables to your values. You can then compile the Python3 script to an executable(I recommend py2exe), as a victim would be more likely to run an executable than a Python3 script. But watch out for the reverse engineers, Python(3) scripts are really easy to reverse engineer, and if someone does, you will most likely get caught.
Have fun using it. 
greetingz,
rusty-s3c/cesar
