import random
month = raw_input("What month were you born in? ")
day = raw_input("What day of the month (1-31)? ")
year = raw_input("What year were you born? ")


dictionary_values = {"animal":["cat", "dog", "aardvark", "giraffe"], "place":["San Francisco", "The North Pole", "Timbuck2"],"personality":["super-nice",
"kind", "funny"],"beauty":["gorgeous","looks like a super model", "most beautiful woman ever"]}
print dictionary_values
print "\n \n Here's your horoscope: \n For someone born on %s %s %s. You are %s and %s. You will live in %s and have a pet %s. " % (month,day,year,random.choice(dictionary_values["beauty"]),random.choice(dictionary_values["personality"]),random.choice(dictionary_values["place"]), random.choice(dictionary_values["animal"]))
