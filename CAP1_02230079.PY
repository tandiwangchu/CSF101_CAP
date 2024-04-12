################################
# Tandin Wangchuk
# Electrical Enginnering Department (First Year)
# 02230079
################################
# Source of Reference/ From where we acquired help
# https://www.youtube.com/watch?v=6i3EGqOBRiU&list=PLdo5W4Nhv31bZSiqiOL5ta39vSnBxpOPT
# https://www.youtube.com/watch?v=Qcefu1jVPds&t=3s
# ChatGPT
# Blackbox.ai
# https://codefinity.com/
# freeCodeCamp
# https://www.tutorialspoint.com/python/index.htm

################################
# Solution/Final_Output
# My Solution Score is :47075
# CSF101_CAP/input_9_cap1.txt
################################# Read the input.txt file
def read_input(Input_your_file_name): # We define a fucntion called "read_input" 
    x = [] # We are just creating an empty list [] that is represented by the letter x
    with open(Input_your_file_name, 'r') as files: # For each line in the file
        for y in files: # We assign a while loop for storing the value of files in the variable y 
            opposition_picked, outcome = y.split() # Create a tuple containing the two parts and append it to the above list and also we use split funtion to split the space in between the upcoming conditions
            x.append((opposition_picked, outcome)) # Create a tuple containing the values of 'opposition_picked' and 'outcome', and append or add it onto the list
    return x # We are returning the list that consists of the variables 'opposition_picked' and 'outcome'

# Calculating the point for each game/round
def calculate_score(Overall_Games_Played): # Calculates a score for our parameter that is "Overall_Games_Played"
    Point = 0 # The starting point for each round is 0 so we assign the variable 'point'  
    for opposition_picked, outcome in Overall_Games_Played: # Iterate/ repeat through each game in the introduced parameter "Overall_Games_Played" 
#defining the value of individual outcome and opponent's choice which is later used in determining the value.
        if outcome == 'X':  # We need to LOSE or The opposition has to WIN
            if opposition_picked == 'A': # Opposition has chosen Rock
                Point += 3 #  Scissor is defeated by Rock so we get 3 points as 3(for picking scissor) + 0(for the fact that we lost) = 3(the point we receive)
            elif opposition_picked == 'B': # Opposition has chosen Paper
                Point += 1  # Rock is defeated by paper thus we obtain 1 point as 1(for picking rock) + 0(for the fact that we lost) = 1(the point we receive)
            elif opposition_picked == 'C': # Opposition has chosen Scissors
                Point += 2 # Paper is defeated by Scissors therefore we get 2 points as 2(for picking paper) + 0(for the fact that we lost) = 2(the point we receive)
        elif outcome == 'Y':  # We need to produce a DRAW meaning  that our 
            if opposition_picked == 'A': # He/She has chosen Rock.
                Point += 4  # Rock gives draw against Rock so we get 4 points as 1(for picking rock) + 3(for the fact that we prodeced a draw) = 4(the point we receive)
            elif opposition_picked == 'B': # He/She has chosen Paper 
                Point += 5  # Paper gives draw against Paper thus we obtain 5 point as 2(for picking paper) + 3(for the fact that we prodcued a draw) = 5(the point we receive)
            elif opposition_picked == 'C': # He/She has chosen Scissors
                Point += 6  # Scissors gives draw against Scissors therefore we get 6 points as 3(for picking scissors) + 3(for the fact that we produced a draw) = 6(the point we receive)
        elif outcome == 'Z':  # We need to WIN
            if opposition_picked == 'A': # He/She has chosen Rock
                Point += 8  # Paper wins against Rock so we get 8 points as 2(for picking paper) + 6(for the fact that we won) = 8(the point we receive)
            elif opposition_picked == 'B': # He/She has chosen Paper
                Point+= 9 # Scissors wins against Paper thus we obtain 9 points as 3(for picking scissors) + 6(for the fact that we won) = 9(the point we receive)
            elif opposition_picked == 'C': # He/She has chosen Scissors 
                Point += 7 # Rock wins against Scissor therefore we get 7 points as 1(for picking rock) + 6(for the fact that we won) = 7(the point we receive)
    print(f"The final accumulation of points is:{Point}") #Printing out the total sum of the points from the input file as we already stored the total accumulation of points in the argument 'Point'
    # We designate f string to call calling/ returning our argument(That is point)

# Running the program( We run our programme based on the python code we wrote for the above situation and we shall receive an output)
Input_your_file_name = "CSF101_CAP/input_9_cap1.txt"  # We store our respected files designated to our respected index numbers into the parameter 'Input_your_file_name'
calculate_score(read_input(Input_your_file_name)) # Calculate the score using the python code we wrote above and we obtained the value from reading the input file
# In our case our designated input file is called in the argument "Input_your_file_name"
# We then add all the points obtained from the given conditions(meaning our code) in the input file 
# Finally we obtain the final amount of points