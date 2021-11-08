import csv
from faker import Faker
import datetime


def datagenerate(records, headers):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # To generate phone numbers
    with open("school_personell_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@fakeschool.com"
            userId = Fname[0].lower() + Lname.lower() + domain_name

            writer.writerow({
                "Email Id": userId,
                "Prefix": fake.prefix(),
                "Name": fake.name(),
                "Birth Date": fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1, 1)),
                "Phone Number": fake1.phone_number(),
                "Zip Code": fake.zipcode(),
                "City": fake.city(),
                "State": fake.state(),
                "Country": fake.country(),
                "Year": fake.year(),
                "Time": fake.time(),
                "Link": fake.url(),
                "Text": fake.word(),
            })


if __name__ == '__main__':
    records = 1000
    headers = ["Email Id", "Prefix", "Name", "Birth Date", "Phone Number",
               "Zip Code", "City", "State", "Country", "Year", "Time", "Link", "Text"]
    datagenerate(records, headers)
    print("Fake Personell CSV complete!")
