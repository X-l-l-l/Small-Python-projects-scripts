import re
import sys

# while True:
#     inp = input("Enter the year you want to check, or 'exit' to stop: ")
#     if inp == 'exit':
#         print("Bye!")
#         break
#     match = re.search("[^0-9]+",inp)
#     if match == None:
#         year = int(inp)
#         if (year-2020)%4 == 0:
#             print("Leap")
#         else:
#             print("Not Leap")
#     else:
#         print("Wrong input!")
        
        
inp = sys.argv[1]
match = re.search("[^0-9]+",inp)
if match == None:
    year = int(inp)
    if (year-2020)%4 == 0:
        print("Leap")
    else:
        print("Not Leap")
else:
    print("Wrong input!")
