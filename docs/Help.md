# Guess You
Welcome to Guess You.
Please follow these steps in play Guess You. 

## System requirements:

Modern Operating System:
 - Windows 7 or 10
 - Mac OS X 10.11 or higher, 64-bit
 - Linux: RHEL 6/7, 64-bit (almost all libraries also work in Ubuntu)
 	
x86 64-bit CPU (Intel / AMD architecture)
4 GB RAM
5 GB free disk space

## Software requirements
**Bash** 
For Mac OS and Linux users this will already be pre installed on your system.

Windows users: Windows users need to have Bash installed. follow these instructions to Install bash.

 1. Right-click the Start menu and select Settings.
 
 2. Select Update & Security.
 
 3. Select For developers on the left side.
 
 4. Select Developer mode.
 
 5. Select Yes to confirm, then wait for the developer package to install.
 
 6. Type Windows Features in the desktop search bar and select Turn Windows Features On Or Off.
 
 7. Check the box beside Windows Subsystem For Linux and select OK.
 
 8. Select Restart now in the dialog box to reboot your computer to apply the changes.
 
 9. Go to the [Microsoft Store]
 10. (https://www.lifewire.com/introducing-the-windows-store-3507015) and select the Linux distribution of your choice. Install it then launch it.
 
 11. Wait for the distribution to finish installing, then create a username in the command window and press Enter. During the first-run process, you'll have to engage in some basic configuration, depending on the distribution. Often, you must specify a username and password.
 
 13. After the installation is successful, close the window and right-click the Start menu, then select Windows PowerShell (Admin).

 14. Type bash in the terminal window and press Enter.

**Python 3**
To install Python 3 on your selected operating system follow to steps on the below link https://installpython3.com/

## How to start the application.

 1. Open the Bash terminal window.
 
 2. Navigate to the directory where you have unzipped
    Guess_You.zip file.

 3. You will need to ensure you have permission to execute the guess_you.sh file. In the terminal window type: *chmod +x guess_you.sh*.  Press enter.
 
 4. To run the programme type: *./guess_you.sh* in the terminal window. 
 
 **NOTE:** If you wish to see additional information during the game,  type:  .*/guess_you.sh inspect*.  This will display the information you have entered and all player names. 
 

## How the game is played. 
The game is going to try and find out who you are.

It will firstly ask you some information about yourself. After that it will continue to ask random questions. on possible features that match you.  Depending on your answers it will try and determine who you are. Once the game has guessed you correctly, you will be able to play again or exit.

## How to play.
1. On the start screen it will ask whether you wish the play or exit.
 
 2. To play the game. Type 'Yes' into the terminal window and press enter. 
 
 3. You will then be prompted to answer a few questions about yourself. It will notify you if you have entered a value that it  was not  exception and display you with possible options.
		**NOTE:** It will ask you to enter your full name, this is to ensure it doesn't mistake you for another player. 

4. Once you have entered the necessary information you will be prompted to either play the game, Add another player or Exit. 

5. To continue with the game type 'Yes' into the terminal window.

6. The game will now ask you random Questions about yourself. After every 3 questions it will attempt to guess your name. If it's incorrect it will continue to ask more questions. If it guesses correctly it will ask whether you would like to play again or exit.

7. Type 'Exit' to go back to the main screen. 

8. If you wish to exit the programme, type 'Exit' again whilst on the main screen. 

## Troubleshooting.
**Failed to start the programme:**

 1. If the following message is displayed during start up:
 *Unable to find files to start the programme. Please refer to help.txt documentation for troubleshooting.*
 You need to ensure that you have got the program_files folder in the directory. Within this folder should contain *guess_you.py and user_data.py* 
 
 3. If the following message is displayed during start up:
" *./guess_who.sh: Permission denied* "
You will need to ensure have execute rights to the file. in the terminal window type chmod +x guess_you.sh*.  Press enter.

**Error message "unable to find user_data.py":**
You will need to ensure that user_data.py is located within the main program folder in your directory. 