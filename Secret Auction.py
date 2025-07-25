Bidders = {

   }

prompt='y'
print(Bidders)
print("Welcome to the Silent Auction")
while prompt== 'y':
   print("Write Your Name")
   Name=input()
   print("Write Your Bid")
   Bid=int(input())
   Bidders.update({Name:Bid})
   print(Bidders)
   print("Do you wish to continue Y/N")
   prompt=input()

HighestBid=0
NameBidder=''
for Bid in Bidders:
   if HighestBid< Bidders[Bid]:
      HighestBid=Bidders[Bid]
      NameBidder=Bid
print("Highest Bid: $" +str(HighestBid))
print("Winner: " + NameBidder)
