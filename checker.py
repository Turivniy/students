#!/usr/bin/python

import logging
import os
import sys


# args_lenth = len(sys.argv)
# print 'Number of arguments:', args_lenth, 'arguments.'
# print 'Argument List:', sys.argv[1]


def check(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    check_items = [0, 12, 13, 17, 18, 59, 60, 99]
    cool_items = []
    for item in content:
        age = item.split(' ')[-1]
        if age in check_items or age < 0 or age > 99:
            cool_items.append(int(age))

    for check_item in check_items:
        if check_item not in cool_items:
            print "{} was not checked!!!".format(check_item)

    counter = 0
    for cool_item in cool_items:
        if cool_item > 99 or cool_item < 0:
            counter += 1
            print 'Cool Item: {}'.format(cool_item)

    if counter < 2:
        print "0 < and (or) > 99 weren't tested. Counter: {}".format(counter)

    cool_items = set(cool_items)
    check_items = set(check_items)
    print 'Items:', list(cool_items - check_items)


if __name__ == "__main__":
    # filename = int(sys.argv[1])
    filename = '/tmp/students_logs/serg.log'
    check(filename)