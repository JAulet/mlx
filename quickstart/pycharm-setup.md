#Setting Up Development Through Pycharm

##Cloning repository

Make sure you have forked the [MLX Repository](https://github.com/machine-learning-exchange/mlx)

###Link Github Account to Pycharm

Go To File > Preferences (Settings for Windows Users) > Version Control > Github

Click the plus in the top-right corner to add your account. 

If you have a Github SSH token, click "Login With Token".

Otherwise, click "Sign in with Github" and follow shown instructions.

##Setup Virtual Environment Within Pycharm

In order to Setup a Virtual Environment, you must first go to Settings 

Then click the dropdown for Project: <NAME OF PROJECT> 

Click on Python Interpreter and click the gear icon next to the dropdown at the top of the window.

Click add > Virtualenv Environment

Specify a location where the virtual enviroment will be stored.

Select the python.exe within your python installation location as base interpreter.

##Set WSL as terminal.

If developing on Windows, you may find it necessary to use Windows Subsystem for Linux. Also known as WSL

To install WSL, follow [these instructions](https://docs.microsoft.com/en-us/windows/wsl/install)

After WSL is installed on your system, in order to change the terminal within PyCharm to WSL, you must:

Go To File > Preferences (Settings for Windows Users) > Tools > Terminal 

Under Shell Path: select bash.exe in its install location.

For example: 

    C:/<YOUR NAME HERE>/System32/bash.exe