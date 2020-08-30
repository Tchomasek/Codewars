def meeting(s):
    list = s.split(";")
    full_name_list = []
    result = ""
    for index, full_name in enumerate(list):
        name,surname = full_name.split(":")
        name=name.upper()
        surname=surname.upper()
        full_name_list.append("{}, {}".format(surname,name))
    full_name_list = sorted(full_name_list)
    for fullname in full_name_list:
        name,surname = fullname.split(",")
        result+="({},{})".format(name,surname)
    return result

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(meeting(s))



"""John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

Could you make a program that

    makes this string uppercase
    gives it sorted in alphabetical order by last name.

When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

It can happen that in two distinct families with the same family name two people have the same first name too."""
