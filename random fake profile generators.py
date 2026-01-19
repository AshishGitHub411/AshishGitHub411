import random

class DataStore:
    def __init__(self):
        self.fname = [
            'John','Jane','Corey','Travis','Dave','Kurt','Neil','Sam','Steve','Tom',
            'James','Robert','Michael','Charles','Joe','Mary','Maggie','Nicole',
            'Patricia','Linda','Barbara','Elizabeth','Laura','Jennifer','Maria',
            'Adam','Sturt','Nikolson','Harry','Ruskin','Thor','Rocky','Ravid',
            'David','Harris','Eion','Elon','Mark','Will','Chris'
        ]

        self.lname = [
            'Smith','Doe','Jenkins','Robinson','Davis','Stuart','Jefferson',
            'Jacobs','Wright','Patterson','Wilks','Arnold','Johnson','Williams',
            'Jones','Brown','Miller','Wilson','Moore','Taylor','Anderson','Thomas',
            'Jackson','White','Harris','Martin','Potter','Jukerberg','Nebula',
            'Downy','Downy Jr'
        ]

        self.street_names = [
            'Main','High','Pearl','Maple','Park','Oak','Pine',
            'Cedar','Elm','Washington','Lake','Hill'
        ]

        self.cities = [
            'Metropolis','Eerie',"King's Landing",'Sunnydale','Bedrock',
            'South Park','Atlantis','Mordor','Olympus','Dawnstar','Balmora',
            'Gotham','Springfield','Quahog','Smalltown','Epicburg',
            'Pythonville','Faketown','Westworld','Thundera','Vice City',
            'Blackwater','Oldtown','Valyria','Winterfell','Braavos','Lakeview'
        ]

        self.states = [
            'AL','AK','AZ','AR','CA','CO','CT','DC','DE','FL','GA','HI','ID','IL',
            'IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE',
            'NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD',
            'TN','TX','UT','VT','VA','WA','WV','WI','WY'
        ]


class FakeProfile:
    def __init__(self, data):
        self.data = data

    def generate_gender(self):
        return random.choice(["Male", "Female"])

    def generate_name(self):
        return f"{random.choice(self.data.fname)} {random.choice(self.data.lname)}"

    def generate_age(self):
        return random.randint(18, 65)

    def generate_address(self):
        house = random.randint(100, 9999)
        street = random.choice(self.data.street_names)
        city = random.choice(self.data.cities)
        state = random.choice(self.data.states)
        return f"{house} {street} St, {city}, {state}"

    def generate_contact(self):
        return f"+1-{random.randint(200,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"

    def generate_email(self, name):
        username = name.replace(" ", ".").lower()
        number = random.randint(1, 999)
        return f"{username}{number}@mail.com"

    def create_profile(self):
        name = self.generate_name()
        return {
            "Name": name,
            "Gender": self.generate_gender(),
            "Age": self.generate_age(),
            "Address": self.generate_address(),
            "Contact": self.generate_contact(),
            "Email": self.generate_email(name)
        }


class ProfileGenerator:
    def __init__(self, count):
        self.count = count
        self.data = DataStore()
        self.profile = FakeProfile(self.data)

    def generate(self):
        print("\n" + "=" * 55)
        print("        RANDOM FAKE PROFILE GENERATOR")
        print("=" * 55)

        for i in range(1, self.count + 1):
            profile = self.profile.create_profile()
            print(f"\n📇 Profile {i}")
            print("-" * 45)
            for key, value in profile.items():
                print(f"{key:<10}: {value}")
            print("-" * 45)


# -------- MAIN PROGRAM --------
try:
    num = int(input("Enter number of fake profiles to generate: "))
    generator = ProfileGenerator(num)
    generator.generate()
except ValueError:
    print("❌ Please enter a valid number.")
