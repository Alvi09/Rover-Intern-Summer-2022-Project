# Rover Intern Summer 2022 Project

## Setup project locally


## Assumptions
  - Profile Score's distinct letters doesn't take in account upper / lower (i.e A and a count as one distinct letter)



## Approach
  - Read in given CSV file using command-line (i.e not inputs) and recreate their 'search algorithm' to create a new csv, sitters.csv, with the correct columns
  - Each important thing is separated by a comma in the CSV file (can probably use .split()) and note that first row is the 'header'
  1) Read through CSV file 
  2) Probably use a list of dictionarys to store [ {email: email, name: name, profile_score: p_s, ratings_score: r_s, search_score: s_s} ] because the same person can sit dogs multiple times
  3) Fill in dict by using the correct indices, and update the scores when needed
  4) Use dict to output a new CSV called sitters.csv

## Libraries used
  - `import csv` to handle reading csv


## Decisions and tradeoffs
  - What data structure should I use to store the information? Should I use a list or a dictionary? What should be the keys, the values?
    - Dictionary sounded much easier to work with, because I can just check, "Hey, is this email in this dictionary? If so, we don't need to create a new one, let's just update the existing values
    
  - Should I try to update the scores in one go? Would it be better to instead, have a function that loops through everything already, and we just call that function whenever we need to?
    - Not sure how to update the score averages in one go, since that'd require the rating / len(how many times the user sat dogs)
    - Probably better to do the latter, but need to take into time complexity since we're looping through a big CSV file again
    
  - Should I store the whole CSV file into a 2D list? Or should I try to parse them on the go?
    - I think store into a 2D list, and use that list whenever we want to access anything from the CSV file
    - Reason for this is bc the file pointer changes, so I can't go back to the top of the CSV file if I wanted to (unless there's a way but I couldn't find atm)

## Features


## Improvements
