from itertools import count


print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
# my_list = [ ] or my_list = list()
counties[0]
# last item print(counties[-1])
##lenght
    len(counties)
    #counties[0:2] 0 and 1 , counties[0:1] just first element  
    #counties[:2] till to 2
    
    
## to add append  list.append("")
    counties.append("El Paso")
    print(counties)
## add to a specific location insert
    counties.insert(2,"Boca Juniors")
    print(counties)
    
    #remove 
    counties.remove("El Paso")
    counties.pop(2)
    print(counties)
    # change 
    counties[2] = "El paso"
    print(counties)
#tuple is a list cannot change
counties_tuple = ("Arapahoe","Denver","Jefferson")
#dictionary my_dictionary = dict()
            #or my_dictionary = {...}
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
len(counties_dict)

#item value key .... counties_dict.values() shows the result
#get a value 
counties_dict.get("Denver")
###################
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
##input automatically str to change it int float etc for calculations.. 
# to print change str again


# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)