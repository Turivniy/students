#!/usr/bin/python

import sys


def check(file_name):

    grade = 12
    invalid_count = 0

    with open(file_name) as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    check_items = [0, 12, 13, 17, 18, 59, 60, 99]
    cool_items = []
    for item in content:
        age = item.split(' ')[-1]
        if item.split(' ')[-3] == 'INVALID':
            invalid_count += 1
        if age in check_items or age < 0 or age > 99:
            cool_items.append(int(age))

    for check_item in check_items:
        if check_item not in cool_items:
            grade -= 1
            print "{} was not checked!!!".format(check_item)

    counter = 0
    for cool_item in cool_items:
        if cool_item > 99 or cool_item < 0:
            counter += 1
            print 'Cool Item: {}'.format(cool_item)

    if counter < 2:
        grade = grade - (2 - counter)
        print "0 < and (or) > 99 weren't tested. Counter: {}".format(counter)

    cool_items = set(cool_items)
    check_items = set(check_items)
    grade_items = list(cool_items - check_items)

    if len(grade_items) < 7:
        grade = grade - 1

    if invalid_count > 3:
        grade += 1

    print 'Items:', grade_items
    print "You grade is: {}".format(grade)


if __name__ == "__main__":
    file_name = sys.argv[1]
    check(file_name)
