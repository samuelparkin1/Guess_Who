Status update 13/07/2021:
The fundamentals of the main functions including New User input, Random question generator, Answer filter and User data base mostly complete.

The User data base is now located in a separate file to help clean up the code. This is now accessible to the other functions.

The New User function is now able to take inputs from the user and verify that it is a correct answer before continuing onto the next question. As the user completes the questions, its associated list/dictionary is appended with the input. Also, a single function has been made to process all New User inputs. As each question is asked, it calls this function and give it the necessary variables to check the answer and update their list or dictionaries. 

The random question generator is mostly complete. It can create random questions base on the information within a temporary data base. Within this temporary data base has a list of dictionaries of the players’ names and their features such as hair colour. As each question is asked, it removes either the single feature or the whole features dictionary depending on the users answer. This I to ensure that the same question does not get asked twice. 
A fault was found during early testing. If the question generator run out of possible questions the program would go into an error. A ‘try/except’ statement has been put in to allow the function to continue. The Question Generator feature has taken a considerable amount of time to complete and has meant a review on the ongoing works schedule to be adjusted. 

The answer filter is still in progress. I still need to think of the best way for this to function, whether it will be in its own function or be incorporated into the question generator function. 

As for ongoing work that needs to be completed, once all features are working independently, I will need to work on how they will flow throughout the program. Followed by testing for faults and errors. 
