"""file_name = input("Enter file name: ")
Search,Replace = input("Enter search string: ").split(" ")
print(Search,Replace)
with open(f"{file_name}", "r") as f:
    data = f.read().splitlines()
    print(data)
    print(f"{file_name}.new")

with open(f"{file_name}.new", "w") as f1:
    for line in data:
        f1.write(line.replace(Search,Replace))
"""
"""months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
with open("timesheet.rtf","r") as f:
    data = f.read()
    print(data)
for month in months:
    with open(f"timesheet_{month}23.rtf", "w") as f1:
        f1.write(data)
"""

"""countries = [{"name": "Spain",
             "capital_city": "Madrid",
             "currency": "EUR"
            },
            {"name": "United States",
             "capital_city": "Washington",
             "currency": "USD"
            },
            {"name": "Canada",
             "capital_city": "Ottawa",
             "currency": "CAD"
            }
           ]
for country in countries:
    for key, value in country.items():
        if key == "name":
            file_name = country[key]
            print(file_name)
            city = country["capital_city"]
            print(city)
            with open(f"{file_name}.txt", "w") as f2:
                f2.write(f"capital_city : {city}")"""
with open("sounds-multiply.csv","r") as f:
    data = f.read().splitlines()
    for index,line in enumerate(data):
        if index != 0:
            Filename, MultiplicationNumer, OutputFilename = line.split(",")
            with open(Filename, "rb") as f3:
                data = f3.read()
            with open(OutputFilename, "wb") as f4:
                for _ in range(int(MultiplicationNumer)):
                    f4.write(data)



