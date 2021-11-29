from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

#dictionary to store the values
bid={}
continue_bid="Yes"


while continue_bid=="Yes":
  name=input("What is your name?: ")
  amt_bid=input("What is your bid amount?: ")
  bid.update({name:int(amt_bid)})
  continue_bid=input("Are there more bidders. Type Yes or No: ")
  if continue_bid=="Yes":
    clear()

print(f" {max(bid)} is the highest bidder with {bid[max(bid)]} amt")

#print(bid)
  
