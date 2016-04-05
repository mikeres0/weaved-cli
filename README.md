# weaved-cli
A command line tool for retrieving Weaved connection information. Written in Python.

##### Dependencies
1. [Python Requests](http://docs.python-requests.org/en/master/) - Installed using `pip install requests`


##### Usage
1. Download the weaved-cli using `git clone https://github.com/mikeres0/weaved-cli.git`
2. Navigate into the directory using `cd weaved-cli`and run using `python weaved.py`
3. Enter your email address and password
4. Select a device from the list
5. Your connection information will be returned like so: `http://proxy**.yoics.net:*****`


###### **Potential issue:** If you recieve the following error, wrap your email address in double quotes, for instance "email@url.com"

```Traceback (most recent call last):
  File "weaved.py", line 69, in <module>
    Init()
  File "weaved.py", line 6, in Init
    username = input("Enter your email address: ")
  File "<string>", line 1
    email@url.com```
