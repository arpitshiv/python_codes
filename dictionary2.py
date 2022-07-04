travl_log=[
    {"country":"france",
    "times_visited":12,
    "cities_visited":["a","b","c"]
    }
]
def add_newcity(country_visited,times_visited,cities_visited):
    new_dic={}
    new_dic["country"]=country_visited
    new_dic["times_visited"]=times_visited
    new_dic["cities_visited"]=cities_visited
    travl_log.append(new_dic)

add_newcity("russia",14,["moscow","sanghai","ussr"])
print(travl_log)