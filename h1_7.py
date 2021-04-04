import datetime

info = {}


def delete_member(name):
    return info.pop(name)


def add_member(name, year, month, day, role):
    info[f'{name}'] = {'birthday': datetime.date(year, month, day,), 'role': role}
    return info


def add_concert(city, year, month, day, *spending, contract=1000000):
    info[f'{city}'] = {'date': datetime.date(year, month, day,),
                       'spending': spending,
                       'contract': contract}
    return info


def calculate_spending(city):
    return sum(info[f'{city}']['spending'])


def calculate_income_of_concert(city):
    return info[f'{city}']['contract'] - sum(info[f'{city}']['spending'])


add_member('Skriptonit', 1994, 1, 1, 'singer')
add_member('Jake', 1990, 10, 11, 'guitarist')
add_member('AndyPanda', 1996, 2, 10, 'singer')
add_concert('Moscow', 2020, 1, 1, 40000, 50000, 90000, 70000)
add_concert('Bishkek', 2020, 2, 14, 30000, 90000, 70000)
add_concert('Nursultan', 2020, 3, 10, 70000, 40000, 100000, 50000)
add_concert('Sank-Peterburg', 2020, 4, 13, 80000, 30000, 40000, 20000, 70000)
add_concert('Yerevan', 2020, 5, 17, 90000, 80000, 90000, 60000)
print(sum([calculate_income_of_concert('Moscow'),
      calculate_income_of_concert('Bishkek'),
      calculate_income_of_concert('Nursultan'),
      calculate_income_of_concert('Sank-Peterburg'),
      calculate_income_of_concert('Yerevan')]))
print(info)


