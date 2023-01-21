#Doesn't need a port ...its not a client or server app
#docker run id ---------- prints line 1 and exits with error
#docker run -i -t id OR -it id ---------- works normally.. -i listens for input through STDIN and -t (optional) binds it to terminal

from random import randint

min_number = int(input('Please enter the min number: '))
max_number = int(input('Please enter the max number: '))

if (max_number < min_number): 
  print('Invalid input - shutting down...') 
else:
  rnd_number = randint(min_number, max_number)
  print(rnd_number)

