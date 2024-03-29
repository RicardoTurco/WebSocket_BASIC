### Updated - Mar/03/20
Python: 3.7


# WebSocket_BASIC
Basic example of WebSocket using Flask and Python 3.4

ATTENTION:  you must install Python 3.4 in your enviroment !!!


Open 2 "terminals" on your computer. In each one go to "WebSocket_SERVER" and "WebSocket_CLIENT" respectively.

Execute these instructions on each one:

- Create and activate virtualenv  

- This next 3 steps are OPTIONAL, but HIGH recommended !!!
1) python -m pip install --upgrade pip
2) pip install -U setuptools
3) pip install wheel

- pip install -r requirements.txt;


RUNNING THE "HELLO" METHOD:  
(Enable the hello method in the app.py file and disable the others. This must be done in SERVER and CLIENT)

In the "WebSocket_SERVER" terminal, when it is executed "python app.py runserver", the terminal will wait:

![](IMGs/001_WebSocketBASIC_SERVERwaiting.png)

In the "WebSocket_CLIENT" terminal, when it is executed "python app.py runserver", the terminal will look like this:

![](IMGs/002_WebSocketBASIC_runCLIENT.png)

When you enter a person's name, the "CLIENT" sends it to the "SERVER", where it will return the message: 

"... Hello NAME ! ..."

![](IMGs/003_WebSocketBASIC_WorkingTogether.png)


RUNNING THE "SOMA" METHOD:  
(Enable the soma method in the app.py file and disable the others. This must be done in SERVER and CLIENT)

In the "WebSocket_SERVER" terminal, when it is executed "python app.py runserver", the terminal will wait:

![](IMGs/001_WebSocketBASIC_SERVERwaiting.png)

In the "WebSocket_CLIENT" terminal, when executed "python app.py runserver", 2 numbers will be sent to SERVER and the result of the "SOMA" method will be returned.

![](IMGs/004_WebSocketBASIC_SendAndReceiveLISTs.png)


RUNNING THE "TESTING_DICT" METHOD:  
(Enable the testing_dict method in the app.py file and disable the others. This must be done in SERVER and CLIENT)

In the "WebSocket_SERVER" terminal, when it is executed "python app.py runserver", the terminal will wait:

![](IMGs/001_WebSocketBASIC_SERVERwaiting.png)

In the "WebSocket_CLIENT" terminal, when running "python app.py runserver", a JSON is sent to SERVER. There, these values are changed and returned to CLIENT:

![](IMGs/005_WebSocketBASIC_SendAndReceiveJSONs.png)
