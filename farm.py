#!/usr/bin/env python3

# loopthat returns all the animals from the NE Farm!

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_animals= farms[0]["agriculture"]

for x in NE_animals:
     print(x)

# asking ro choose whihc farm

for farm in farms:
    print("-", farm["name"])
choice= input("Pick a farm!\n")

for farm in farms:
    if farm["name"].lower() == choice.lower():
        print("Done")


