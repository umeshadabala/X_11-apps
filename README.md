# X_11-apps

**X_11-apps** is a versatile Python-based desktop application built using Tkinter. It serves as an all-in-one utility tool, featuring a range of sub-applications such as a calculator, paint app, browser, notepad, to-do list, and games like Snake and Tic-Tac-Toe. Additionally, it provides system controls like shutdown and restart.

### Use Case for CLI-Based OS
This application is particularly useful for **CLI-based operating systems** (e.g., minimal Linux distributions) where users may need access to essential tools without the overhead of a full desktop environment. X_11 GUI enables users to launch utilities through a graphical interface, making it a powerful addition for systems typically operated via the command line.

## Table of Contents
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Included Sub-Applications](#included-sub-applications)
- [System Requirements](#system-requirements)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Graphical User Interface** using Tkinter.
- **Multiple Sub-Applications** including:
  - Calculator
  - Paint
  - Browser
  - To-Do List
  - Notepad
  - IDE
  - File Manager
  - Camera
  - Media Player
  - Sheets
  - Games like Snake, Sudoku, and Tic-Tac-Toe (XoX)
- **System Commands** like Shutdown and Restart.
- **Clock Display** showing real-time hours, minutes, and seconds.
- **Image-Based Buttons** for easy navigation.
- **Background Image** for enhanced aesthetics.



## Installation
1. **Python 3.9 or higher** is required to run the application. If you don't have Python installed, download it from [here](https://www.python.org/downloads/).
2.Create a **virtual enviorment** and running the app :
```bash
git clone https://github.com/umeshadabala/X_11-apps.git
cd X_11-apps
sudo apt install python3-venv
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
python main.py
```
### Running the Application
Once the application is running, you'll see a window with a grid of image-based buttons. Each button launches a corresponding sub-application or performs a system operation.

### How to Use:
Click on any button to launch the corresponding application.
The shutdown and restart buttons will control your system as per your OS settings.
The clock is displayed at the bottom of the window, showing the current time.
Included Sub-Applications
Calculator: A simple calculator app for basic arithmetic operations.
Paint: A basic paint program to draw and sketch.
Browser: A simple web browser.
Notepad: A basic text editor.
To-Do List: Manage and keep track of your tasks.
Snake Game: Play the classic Snake game.
Tic-Tac-Toe (XoX): A two-player XoX game.
IDE: A lightweight Python IDE.
File Manager: Browse and manage your files.
Camera: Take pictures using your computer's camera.
Media Player: Play media files.
Sheets: Simple spreadsheet functionality.
Sudoku: Play the classic Sudoku puzzle game.
Info: Display information about the app.
### System Requirements
 OS: Windows, Linux
 <br>
 Python Version: 3.9 or higher
 
### Optimized for CLI-Based OS:
X_11 GUI can be run in CLI-based operating systems that may lack a full-fledged desktop environment, providing users access to essential tools through an intuitive GUI.

```bash
chmod +x install.sh
./install.sh
```

### Drwabacks:-
1.Can't run multiple applications at one time.
2.To run a second application the first application should be closed.
3.When a application is open the main applications gets stuck.
We are sorry for the inconvenience cause by the drawbacks we'll get a solution for these bugs in the next version as soon as possible.

### Common errors:
1.If the browser doesnt work then try these these command:-
```bash
sudo apt-get install libqt5webengine5 libqt5quick5
```
2.Starting an X server :-
2.1(FOR A VM):-
```bash
sudo apt install xauth
sudo nano /etc/ssh/sshd_config
X11Forwarding yes #you need to edit it in two places in the script
X11DisplayOffset 0
X11UseLocalhost yes
sudo system restart ssh
ssh -X username@remote_host
python3 main.py
```
2.2(FOR LOCAL SYSTEM):-
```bash
sudo apt-get update
sudo apt-get install xorg openbox
sudo apt-get install xterm xauth openssh-server 
sudo nano /etc/ssh/sshd_config
X11Forwarding yes #you need to edit it in two places in the script
X11DisplayOffset 0
X11UseLocalhost yes
sudo system restart ssh
startx
ssh -X username@local_host
python3 main.py
```
### Credits
Special thanks to Flaticon[https://www.flaticon.com/] for the images.
### Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. You can also open issues for bug reports or feature requests.

### License
This project is licensed under the MIT License.
