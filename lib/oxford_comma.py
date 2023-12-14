def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return ' and '.join(items)
    else: oxford = ', '.join(items[:-1]) + ', and ' + items[-1]
    return oxford

print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))
