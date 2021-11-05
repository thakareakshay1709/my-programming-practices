
LKP =[
    {
        "country": "ie",
        "cities": ["dublin", "limeric", "galway"]
    },
    {
        "country": "us",
        "cities": ["chicago", "another"]
    }
]


def get_country_name(city):
    for items in LKP:
        if city in items["cities"]:
            return items["country"]


print(get_country_name("chicago"))
