#!usr/bin/env python3

from plumbum import local, colors
import sys
import os

def show_venv_exists_error():
    print(colors.orchid | '[Virtual Environment Already Exists]')
    print()
    print(colors.yellow | '  A .venv folder was found, signifying a virtual environment likely exists.')
    print(colors.yellow | '  Look through the contents of that folder and backup/delete it if needed.')

def show_gitignore_exists_error():
    print(colors.orchid | '[gitignore Already Exists]')
    print()
    print(colors.yellow | '  A .gitignore file was found.  Look through the contents of that file')
    print(colors.yellow | '  and backup/delete it if needed.')

def show_script_exists_error():
    print(colors.orchid | '[Script Already Exists]')
    print()
    print(colors.yellow | '  The given file already exists in the current directory.  Look through the')
    print(colors.yellow | '  contents of that file and backup/delete it if needed.')

def show_help_text():
     print(colors.orchid | '[Friendly Help Message]')
     print()
     print(colors.yellow | 'Usage: python3 scaffoldpyscript.py <script-name>')
     print(colors.yellow | '  scaffoldpyscript is used to start up a new script body with directories such')
     print(colors.yellow | '  as .venv and .github already made.  It also comes with some helper tips to get')
     print(colors.yellow | '  the development process started.')
     print()
     print(colors.green| '  Shell script originally made by Olin Gallet April 2022')

def show_intro_text():
     print(colors.blue | '==*== Let\'s make a Python script!  Scaffolding with .gitignore, .venv, and a skeleton file! ==*==')
     print(colors.orchid | '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣀⣀⣶⣄')
     print(colors.orchid | '⠀⠀⠀⠀⠀⠀⠀⢀⡠⣔⠮⠍⠛⠒⠒⠒⠚⠠⠽⣉⠙⠻⢿⣿⣿⣷')
     print(colors.orchid | '⠀⠀⠀⠀⠀⣠⡂⠕⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠢⢀⡹⠛⠋⠑⡄')
     print(colors.orchid | '⠀⣀⣀⣠⣼⠏⠀⠀⠀⠀⠀⠀⠀⠜⠑⣄⠀⠀⠀⠀⠀⠠⠊⠀⠀⠀⠀⣷')
     print(colors.orchid | '⣿⣿⣿⣿⡏⠀⠀⠀⢸⠉⢆⠀⠀⢸⣀⣸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏')
     print(colors.orchid | '⣿⣿⣿⣿⠃⠀⠀⠀⠸⣄⣸⡆⠀⠈⢿⣿⣿⠀⣠⣴⣶⣶⡄⠀⢀⣤⣾⣇⣀⣀⡀')
     print(colors.orchid | '⣿⣿⣿⣿⣦⣄⠀⠀⠀⢻⣿⣿⠀⠀⠈⠻⡿⠀⠘⠛⠛⠋⠁⠸⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⡿⢿⣿⣿⣷⢀⣀⠀⠻⠿⢀⣴⣶⣶⡆⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣦⣤⠛⣿⣿⣿⡿⠃⠀⠀⠹⣿⣿⣿⠇⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣿⣿⣦⡈⣿⣿⠇⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃')
     print(colors.orchid | '⠉⠻⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃')
     print(colors.orchid | '⠀⠀⠀⠀⠛⢿⣿⣿⣿⣷⢦⣄⣀⡀⠤⣤⣤⣀⣀⣬⣿⣿⣿⣿⣿⣿⣿⠟⠁')
     print(colors.orchid | '⠀⠀⠀⢠⣴⣿⣿⣿⣿⣿⣦⣭⣷⣶⣿⣿⡿⠿⠟⠋⠁⠉⠛⠛⠿⠋⠁')
     print(colors.blue | '==*== Updated April 2022 <3 <3 <3 ==*==')

def show_outro_text():
     print(colors.blue | '==*== Scaffolding complete! ==*==')
     print(colors.orchid | '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣀⣀⣶⣄')
     print(colors.orchid | '⠀⠀⠀⠀⠀⠀⠀⢀⡠⣔⠮⠍⠛⠒⠒⠒⠚⠠⠽⣉⠙⠻⢿⣿⣿⣷')
     print(colors.orchid | '⠀⠀⠀⠀⠀⣠⡂⠕⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠢⢀⡹⠛⠋⠑⡄')
     print(colors.orchid | '⠀⣀⣀⣠⣼⠏⠀⠀⠀⠀⠀⠀⠀⠜⠑⣄⠀⠀⠀⠀⠀⠠⠊⠀⠀⠀⠀⣷')
     print(colors.orchid | '⣿⣿⣿⣿⡏⠀⠀⠀⢸⠉⢆⠀⠀⢸⣀⣸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏')
     print(colors.orchid | '⣿⣿⣿⣿⠃⠀⠀⠀⠸⣄⣸⡆⠀⠈⢿⣿⣿⠀⣠⣴⣶⣶⡄⠀⢀⣤⣾⣇⣀⣀⡀')
     print(colors.orchid | '⣿⣿⣿⣿⣦⣄⠀⠀⠀⢻⣿⣿⠀⠀⠈⠻⡿⠀⠘⠛⠛⠋⠁⠸⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⡿⢿⣿⣿⣷⢀⣀⠀⠻⠿⢀⣴⣶⣶⡆⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣦⣤⠛⣿⣿⣿⡿⠃⠀⠀⠹⣿⣿⣿⠇⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣿⣿⣦⡈⣿⣿⠇⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
     print(colors.orchid | '⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃')
     print(colors.orchid | '⠉⠻⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃')
     print(colors.orchid | '⠀⠀⠀⠀⠛⢿⣿⣿⣿⣷⢦⣄⣀⡀⠤⣤⣤⣀⣀⣬⣿⣿⣿⣿⣿⣿⣿⠟⠁')
     print(colors.orchid | '⠀⠀⠀⢠⣴⣿⣿⣿⣿⣿⣦⣭⣷⣶⣿⣿⡿⠿⠟⠋⠁⠉⠛⠛⠿⠋⠁')
     print(colors.blue | '==*== Remember to use "source /bin/sh/activate" to see options to start the venv! ==*==')
     print(colors.blue | '==*== Remember to use "pip3 freeze" to write dependences to requirements.txt ==*==')

def create_venv_folder():
     command = local['python3']['-m', 'venv', '.venv']
     print(colors.yellow | '  Creating .venv folder. . .')
     command.run()[1]
     print(colors.yellow | '  .venv folder created!')

def create_gitignore_file():
     print(colors.yellow | '  Creating .gitignore file. . .')
     with open('.gitignore', 'w') as fp:
         fp.write('.gitignore\n')
         fp.write('.venv\n')
     print(colors.yellow | '  .gitignore file created!')

def create_script_file(script_name):
    print(colors.yellow | f'  Creating file {script_name}')
    with open(script_name, 'w') as fp:
        fp.write('#!/usr/bin/env python3\n')
        fp.write('\n')
        fp.write('# Author: {your name}\n')
        fp.write('# Date: {date today} \n')
        fp.write('\n')
        fp.write('\n')
        fp.write("if __name__ ='__main__':")
    print(colors.yellow | f'  File {script_name} created!')

if __name__ == '__main__':
     if len(sys.argv) != 2:
          show_help_text()
     elif os.path.isdir('.venv'):
          show_venv_exists_error()
     elif os.path.isfile('.gitignore'):
          show_gitignore_exists_error()
     elif os.path.isfile(sys.argv[1]):
          show_script_exists_error()
     else:
          show_intro_text()
          script_name = sys.argv[1]
          if not script_name.endswith('.py'):
              script_name = script_name + '.py'
          print(colors.orchid | '[Starting file creation!]')
          create_venv_folder()
          create_gitignore_file()
          create_script_file(script_name)
          print(colors.orchid | '[Ending file creation!]')
          show_outro_text()
