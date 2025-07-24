import os
import random
import time

Duration=0
while Duration<30:
   icons = ["🍒", "🍋", "🔔", "🍇", "🍉", "⭐", "7️⃣", "💎", "🍀", "🎰"]
   Result=[]
   for index in range(3):
      Result.append(icons[random.randint(0,len(icons)-1)])
   os.system('cls')
   print(Result)
   time.sleep(0.1)
   Duration+=1
 