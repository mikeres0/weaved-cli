# weaved-cli
A command line tool for retrieving Weaved connection information. Written in Python.

##### Dependencies
1. [Python Requests](http://docs.python-requests.org/en/master/) - Installed using `pip install requests`


**Potential issue:** If you recieve the following error, wrap your email address in double quotes, for instance "email@url.com"

```Traceback (most recent call last):
  File "weaved.py", line 69, in <module>
    Init()
  File "weaved.py", line 6, in Init
    username = input("Enter your email address: ")
  File "<string>", line 1
    email@url.com```
