#youtuber = "Alakh Bhatt"
#print(f"Subscribe to {youtuber}")

# adjective = input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famousPerson = input("Famous person: ")
# madlib = f"Computer programming is so {adjective}! \
#      It makese me so excited all the time because I love to {verb1}. \
#      Stay hydrated and {verb2} like you are {famousPerson}!"

# print(madlib)

from sample_madlibs import hp, code, hungergames, zombie
import random

if __name__ == "__main__":
    m = random.choice([hp, code, hungergames, zombie])
    m.madlib()