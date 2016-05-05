"""
Project01B
Author: Ian Davidson CS-115
Description: Using for-loops and user input to rate movies with IMDB's movie rating system. Later displaying which
sequel is highest and lowest rated and the most popular.
"""

def main():

    print("Welcome to movie sequel rating system!")  # welcomes user
    movie_series = input("Which movie series would you like to rate? ")  # Asks which movie series
    movie_series = ("--" + movie_series + "--")  # update movie form
    # asks amount of sequals
    Amount_Series = int(input("How many sequels are there in the movie " + movie_series + " ? "))
    print()                 #empty print command for formatting
    print("You will enter average rating (between 1-10) and number of votes for each of the sequel")
    print()                 #empty print command for formatting
    M = 25000
    C = 7.0
    Total_Score = 0
    Best_rating = 0
    Best_sequel = 0
    Worst_sequel = 0
    Worst_rating = 10
    Votes_sequel  = 0
    Most_Votes = 0
    for i in range(Amount_Series):  # for loop for each sequel
        Amount_Vote = int(          #collects votes from user
            input("Enter the number of votes movie " + movie_series + " sequel " + str(i + 1) + " received: "))
        Sequel_Score = float(       #collects avg score from user
            input("Enter the average user rating of movie " + movie_series + " sequel " + str(i + 1) + ": "))
        #Calculates Weighted Rating, using IMDB's system
        Weighted_Rating = (Amount_Vote/(Amount_Vote + M)) * Sequel_Score + (M/(Amount_Vote + M))*C
        Total_Score += Weighted_Rating  #collects the total score for avg later
        #finds & stores sequel with best weighted rating
        if (Weighted_Rating > Best_rating):
            Best_rating = Weighted_Rating
            Best_sequel = (i + 1)
        #finds & stores sequel with worst weighted rating
        if (Weighted_Rating <= Worst_rating):
            Worst_rating = Weighted_Rating
            Worst_sequel = (i + 1)
        #finds sequel with most votes
        if (Amount_Vote > Most_Votes):
            Most_Votes = Amount_Vote
            Votes_sequel = (i + 1)
        #Prints weighted score
        print("Weighted score of this sequel as per IMDB's formula is " + str(Weighted_Rating))
        print()
    print("Overall rating considering all sequels of movie" , movie_series, " is " , Total_Score/Amount_Series)
    print("Best sequel is #" + str(Best_sequel))
    print("Worst sequel is #" + str(Worst_sequel))
    print("Most popular sequel is #" + str(Votes_sequel))
main()
