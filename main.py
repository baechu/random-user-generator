from __future__ import print_function

__author__ = 'yeol'

import csv
import random


print(
    "Currency will be chosen at random. \n Full names, roles and languages will be generated randomly. \n Users password will be the same as their name.")

amount = int(raw_input("Enter the amount of the users you wish to generate: "))
email = (raw_input("Enter your email: "))
print()

names = ["Uwe", "Tobias", "Max", "Felix", "Jakob", "David", "Paul", "Artem", "Ivan", "Nathan", "Adam", "Louis", "Lucas",
         "Oscar", "Victor", "Oliver", "Jack", "Harry", "Charlie", "Thomas", "Oscar", "James", "George", "Conor", "Ryan",
         "Liam", "Luke", "Kacper", "Filip", "Jan", "Szymon", "Antoni", "Wojtek", "Alek", "Gabriel", "Dylan", "Anna",
         "Hannah", "Sophie", "Emma", "Sarah", "Marie", "Lena", "Laura", "Mia", "Louise", "Elise", "Julie", "Nina",
         "Lana", "Petra", "Amelia", "Olivia", "Emily", "Jessica", "Hanna", "Anna", "Zuzanna", "Julia", "Zofia",
         "Natalia", "Wiktoria", "Gabriela", "Elsa", "Alice"]

surnames = ["Muller", "Schmidt", "Schneider", "Fischer", "Meyer", "Weber", "Schulz", "Wagner", "Becker", "Hoffmann",
            "Gruber", "Bauer", "Steiner", "Fuchs", "Reiter", "Wimmer", "Lang", "Wolf", "Murphy", "Kelly", "Sullivan",
            "Smith", "McCarthy", "Nowak", "Mazur", "Young", "King", "Campbell", "Phillips", "Evans", "Turner"]

roles = ["translator", "administator", "project_manager", "tm_expert"]

currencies = ["USD", "EUR"]

languagecode = ["en_US", "pl_PL", "en_GB", "fr_FR"]

header = ["Title", "First Name", "Last Name", "Job Title", "Roles", "Username", "Password",
          "E-mail address", "Address 1", "Address 2", "City", "State/County", "Postcode/ZIP", "Country",
          "Phone 1", "Phone 2", "Mobile phone", "Fax number", "WWW", "Skype", "MSN", "Language Combinations",
          "Qualifications", "Domains", "TM Access Rights", "Terminology Access Rights", "Customers"]

with open('testusers.csv', 'wb') as csvfile:
    peoplewriter = csv.writer(csvfile, delimiter=';',
                                quotechar=';', quoting=csv.QUOTE_MINIMAL)
    peoplewriter.writerow(header)

    for _ in range(amount):

        username_password = (random.choice(names))
        row = ["", username_password, random.choice(surnames), "Linguist", random.choice(roles), username_password, username_password,
              email, "", "", "", "", "", "GBR", "", "", "", "", "", "", "", "->".join(random.sample(languagecode, 2)),
              "", "", "", "", ""]
        peoplewriter.writerow(row)
        print(row)
        print()

print("Done. Saved as testusers.csv")