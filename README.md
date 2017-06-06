# weaved-cli
A command line tool for retrieving [remot3.it](https://www.remot3.it) (formerly [Weaved](https://www.weaved.com)) connection information. Written in Python.

Note that this is a bit hacky with using a demo API key that I got back in 2015... So it could stop working at any time. I'm sure Remot3 will provide you with a new key should you need it. 

##### Dependencies
1. [Python Requests](http://docs.python-requests.org/en/master/) - Installed using `pip install requests`


##### Usage
1. Download the weaved-cli using `git clone https://github.com/mikeres0/weaved-cli.git`
2. Navigate into the directory using `cd weaved-cli`and run using `python weaved.py`
3. Enter your email address and password
4. Select a device from the list
5. Your connection information will be returned like so: `http://proxy**.yoics.net:*****`

#### Python Version
This script may not run on python 3.5, I'm yet to investigate. 

