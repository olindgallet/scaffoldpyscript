# About scaffoldpyscript.py

`scaffoldpyscript.py` is a script for creating a Python3 script.  These scripts are intended to aid programmers and may reside in the /usr/bin for ease of use.

# Installing scaffoldpyscript.py in Linux

1.  Open a terminal then navigate to your download folder.
2.  Run `wget https://raw.githubusercontent.com/olindgallet/scaffoldpyscript/main/scaffoldpyscript.py` to download the file.
3.  Run `chmod +x scaffoldpyscript.py` to make the file executable.
4.  Run `sudo mv scaffoldpyscript.py /usr/bin/scaffoldpyscript`.  This moves the script into the `/usr/bin/` folder so that users can use the script from the command line.  If you want to install it for only the local user, use `/usr/local/bin` instead.
5.  Verify that the file has moved by typing `scaffoldpyscript`.  If successful, then the script will run and display some help text.

# Using scaffoldpyscript.py

1.  Open a terminal and navigate to your work folder.
2.  [Optional] Make the project folder with `mkdir <project-name>`.
3.  Run `cd <project-name>` to change directory into the app.
4.  Run `scaffoldpyscript`.
