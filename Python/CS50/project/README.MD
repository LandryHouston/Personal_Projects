# Survey

### Video Demo: https://youtu.be/IuVrw5Wrkjo

>#### This is a simple python program that asks for user input such as name, city, state, ect. Then checks the users inputs to make sure they're valid and if correct, submits them to a csv file.

First the program will ask for your First Name.

Second the program will ask for your Last Name.

Third the program will ask for your Date of Birth.

Followed by asking for your City, State, and Zip Code.

Example:

    First Name:
    Last Name:
    Date of Birth (mm/dd/yyyy):
    City:
    State:
    Zip code:

It will then test the inputs to make sure they are valid.

The dob and zip code will get tested through a regular expression.

The City and State will get tested using an if statement to see if they
match the contents in the associated list.

After the inputs are verified as valid, the program will display the users inputs and ask if they are correct.

Example:

    Your name is: First Last
    Born: 01/01/2001
    You live in: San Francisco, California 10101
    Is this correct? (yes/no)

If the user says that the information is correct by typing "yes", the inputs are then stored neatly in a csv file. In this case the csv file is called "project_output.csv".

Example:

    first,last,dob,city,state,zip

If the user says that the information is NOT correct (such as types "no"), the program will then ask you to "Please Try Again" and will run the program again from the start.

At any point in the program if the users inputs do not match the specific criteria, the program will exit and display the reason why.

Example:

    Date of Birth (mm/dd/yyyy): cat
    Invalid DOB

or

    City: California
    Invalid City

Thank you for reading!