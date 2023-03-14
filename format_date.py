def format_date(str_date):
    month, day, year = str_date.split("/")
    return f"{year}-{day}-{month}"

print(format_date("27/05/2005"))
print(format_date("22/08/2004"))
print(format_date("21/02/2005"))
