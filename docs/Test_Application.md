# Test Application

## Scenario 1:

The User input, Question generator and Answer checker function all rely on information from user_data.py file. This test scenario will test what happens if the file is unable to be opened or located. To perform this test, the import function of user_data will be removed. This will simulate the file not being accessible.

Expectations - It is expected that the program will income an error once the user starts to input their information. There is a Try and Except function that has been to in place to catch any NameErrors. As part of this Except function it should display a message to the user and prompt them to exit the program.

Results – The program started up as normal and prompted the user if they would like to continue. It goes on to ask for the user to input their name. When the name is entered the program displays the message “Unable to find user_data.py. Please ensure file is in the correct location. Press Enter to exit program”. Because the program did not crash this test has been successful

## Scenario 2:

The inspect function that can be activated as an argument during the start-up of the program using bash. If the user inputs the argument “inspect” it will display to the user extra information.
The following test will see what happens if no argument are given during the start-up of the Bash Scritp.

Expectations – Because no argument will be given to the program, all input variables will stay blank and this should no effect how the program will works.

Results- ERROR: IndexError: list index out of range.
Because the program is expecting an input from the argument the program crashed.

Resolution - Where the argument is called on, it has now been put into a try and except function. It will try to preform the action and if not successful it will except an IndexError and give the variable that was asking for the argument a false input.

Result- Success. The program now runs without errors and as intended.