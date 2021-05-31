# ljust 靠左對齊(字串在最左邊), rjust 靠右對齊(字串在最右邊)
# ljust center rjust can only be used by type str, so
# we can str(object) to make the function run.
def printpicnic(itemsdict, leftwidth, rightwidth):
    print('PICNIC ITEMS'.center(leftwidth + rightwidth, '-'))
    for k, v in itemsdict.items():
        print(type(k), type(v))
        print(k.ljust(leftwidth, '.') + str(v).rjust(rightwidth))

picnicitems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printpicnic(picnicitems, 12, 5)
printpicnic(picnicitems, 20, 6)