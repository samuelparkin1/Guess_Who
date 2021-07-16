# Development log

 

## Status update 13/07/2021:

The fundamentals of the main functions including New User input, Random question generator, Answer filter and User data base mostly complete. 

The User data base is now located in a separate file to help clean up the code. This is now accessible to the other functions.

The New User function is now able to take inputs from the user and verify that it is a correct answer before continuing onto the next question. As the user completes the questions, its associated list/dictionary is appended with the input. Also, a single function has been made to process all New User inputs. As each question is asked, it calls this function and give it the necessary variables to check the answer and update their list or dictionaries.

The random question generator is mostly complete. It can create random questions base on the information within a temporary data base. Within this temporary data base has a list of dictionaries of the players’ names and their features such as hair colour. As each question is asked, it removes either the single feature or the whole features dictionary depending on the users answer. This I to ensure that the same question does not get asked twice.

A fault was found during early testing. If the question generator run out of possible questions the program would go into an error. A ‘try/except’ statement has been put in to allow the function to continue. The Question Generator feature has taken a considerable amount of time to complete and has meant a review on the ongoing works schedule to be adjusted.

The answer filter is still in progress. I still need to think of the best way for this to function, whether it will be in its own function or be incorporated into the question generator function.

As for ongoing work that needs to be completed, once all features are working independently, I will need to work on how they will flow throughout the program. Followed by testing for faults and errors.

## Status update 16/07/2021:
All functions are now working in sync and functioning correctly.

The program now has a start page that displays a logo and ask if the user would like to continue.

As the user moves on it will asks the user to input their information and ask if they would like to continue with the game, enter a new player or exit. If the user chooses to add a new player if will restart the user input loop. If the user wants to exit it will go back to the start page. When the user proceeds from the main the game will start.

I have also made the screen clear after each question. This was to make it more visually appealing to the user.

For the program to fail successfully there have been multiple Try and Except functions put in throughout the code.

A bash script has also been developed to allow the user to start up the program.

An additional feature has been included into the program that allow the user to see more information during the game. This feature utilizes an argument inputted from the bash script. When the user starts the program with the argument "inspect" it will display the inputted data from the user and see the list of possible names that meet the criteria while the questions are being asked.  

This led to a test scenario to see what would happen if the bash script was started without an argument. This presented a flaw within the program and cause the program to crash. an additional Try/Except function was put in to overcome this issue and allow the game to be played.

The code size has grown considerably as the program has progressed. While the code does work correctly, I believe there are some adjustment that could be made to reduce the size of the code. But as the code still preforms as intended, this will only be attempted once all documentation is completed.