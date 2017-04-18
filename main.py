#!/usr/bin/python

import logging
import os
import sys

username = os.environ['USER']

# args_lenth = len(sys.argv)
# print 'Number of arguments:', args_lenth, 'arguments.'
# print 'Argument List:', sys.argv[1]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('/tmp/students_logs/{}.log'.format(username))
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('[%(asctime)s] [{}] %(message)s'.format(username))
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


def count_prize(age):

    if type(age) is not int:
        print "Not integer. Enter valid value"
        return -1

    if age in [0, 12, 13, 17, 18, 59, 60, 99] or age < 0 or age > 99:
        logger.info('BORDER VALUE Age is: {}'.format(age))

    if age not in range(0, 100):
        logger.info('Age is: {}'.format(age))
        print "Not in range 0, 99. Enter valid value"
        return -1

    if age in range(0, 13):
        print "Children. Your payment is 10$ per month"
        prize = 10
        logger.info('Age is: {}'.format(age))
        return prize

    if age in range(13, 18):
        print "Teens. Your payment is 20$ per month"
        prize = 20
        logger.info('Age is: {}'.format(age))
        return prize
    if age in range(18, 60):
        print "Adults. Your payment is 30$ per month"
        prize = 30
        logger.info('Age is: {}'.format(age))
        return prize

    if age in range(60, 100):
        print "Pensioners. Your payment is 40$ per month"
        prize = 40
        logger.info('Age is: {}'.format(age))
        return prize


if __name__ == "__main__":
    argument = int(sys.argv[1])
    count_prize(argument)

    # assert count_prize(7) == 10
    # assert count_prize(15) == 20
    # assert count_prize(22) == 30
    # assert count_prize(70) == 40
    #
    # assert count_prize(0) == 10
    # assert count_prize(12) == 10
    #
    # assert count_prize(13) == 20
    # assert count_prize(17) == 20
    #
    # assert count_prize(18) == 30
    # assert count_prize(59) == 30
    #
    # assert count_prize(60) == 40
    # assert count_prize(99) == 40