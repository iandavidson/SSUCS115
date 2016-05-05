"""
Project01 partA
Author: Ian Davidson CS-115
Description: Using for-loops and user input to rate movies with IMDB's movie rating system.
"""

def main():

    print("Welcome to movie sequel rating system!")  # welcomes user
    Movie_Series = input("Which movie series would you like to rate? ")  # Asks which movie series
    Movie_Series = ("--" + Movie_Series + "--")  # update movie form
    # asks amount of sequals
    Amount_Series = int(input("How many sequels are there in the movie " + Movie_Series + " ? "))
    print()                 #empty print command for formatting
    print("You will enter average rating (between 1-10) and number of votes for each of the sequel")
    print()                 #empty print command for formatting
    M = 25000
    C = 7.0

    for i in range(Amount_Series):  # for loop for each sequel
        Amount_Vote = int(          #collects votes from user
            input("Enter the number of votes movie " + Movie_Series + " sequel " + str(i + 1) + " received: "))
        Sequel_Score = float(       #collects avg score from user
            input("Enter the average user rating of movie " + Movie_Series + " sequel " + str(i + 1) + ": "))
        #Calculates Weighted Rating, using IMDB's system
        Weighted_Rating = (Amount_Vote/(Amount_Vote + M)) * Sequel_Score + (M/(Amount_Vote + M))*C
        #Prints weighted score
        print("Weighted score of this sequel as per IMDB's formula is " + str(Weighted_Rating))
        print()
main()
