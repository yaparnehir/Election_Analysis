counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
   
   
   
for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county, voters)