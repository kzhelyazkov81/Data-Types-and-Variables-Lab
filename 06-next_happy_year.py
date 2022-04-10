year = int(input())
happy_year = False

while not happy_year:
    year += 1
    str_year = str(year)
    set_str_year = set(str_year)
    if len(str_year) == len(set_str_year):
        happy_year = True

print(year)
