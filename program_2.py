# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    # WRITE YOUR CODE HERE
    ######################

total_tickets= 0

keep_going= 'y'

while keep_going==('y'):
    movie_name= (input("Enter movie name(or done, if already selected movie):"))
    tickets= int(input(f"How many tickets would you like?"))
    keep_going= input('Do you want to see another movie(enter y for yes):')
# I am a little confused about how to get the tickets to add each other, Specifically the one input.
total_tickets += tickets

print('The amount of tickets wanted:',total_tickets)
