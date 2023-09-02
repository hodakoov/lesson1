def get_summ(one, two, delimiter='&'):
    one = str(one).capitalize()
    two = str(two).capitalize()
    return(one+delimiter+two)

r = get_summ("Learn","python")
print(r)