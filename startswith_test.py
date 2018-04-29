country_list = ['Германия (111)', 'Австрия (234)', 'Франция (444)']

country = ""
while country != "close":
    # country = str.capitalize(input("страна: "))
    country = input("страна: ")
    # австралия ->> Австралия
    country = country.capitalize()

    for i in country_list:
        if i.startswith(country):
            print(i, "=", country)
            break
