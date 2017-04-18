#!/usr/bin/python

import logging
import os
import sys

username = os.environ['USER']

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('/tmp/students_logs/{}_v3.log'.format(username))
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('[%(asctime)s][v3][{}] %(message)s'.format(username))
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


def count_prize(age):

    try:
        age = int(age)
    except ValueError:
        logger.info('INVALID VALUE: -1')
        print "\n\tNot integer. Enter valid value\n"
        return -1

    if age in range(0, 13):
        print "\n\tChildren. Your payment is 10$ per month\n"
        prize = 10
        logger.info('Age is: {}'.format(age))
        return prize

    if age in range(13, 18):
        print "\n\tTeens. Your payment is 20$ per month\n"
        prize = 20
        logger.info('Age is: {}'.format(age))
        return prize
    if age in range(18, 60):
        print "\n\tAdults. Your payment is 30$ per month\n"
        prize = 30
        logger.info('Age is: {}'.format(age))
        return prize

    if age in range(60, 100):
        print "\n\tPensioners. Your payment is 40$ per month\n"
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