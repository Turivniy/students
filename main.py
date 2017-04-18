#!/usr/bin/python

import logging
import os
import sys

username = os.environ['USER']

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('/tmp/students_logs/{}.log'.format(username))
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - {} - %(message)s'.format(username))
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


def count_prize(age):
    # logger.info('======================')
    # logger.info('Age is: {}'.format(age))
    if type(age) is not int:
        return -1

    if age not in range(0, 100):
        print "Enter valid value"
        return -1

    if age in range(0, 13):
        print "Children. Your payment is 10$ per month"
        prize = 10
        logger.info('Age, Prize is: {} {}'.format(age, prize))
        return prize

    if age in range(13, 18):
        print "Teens. Your payment is 20$ per month"
        prize = 20
        logger.info('Age, Prize is: {} {}'.format(age, prize))
        return prize
    if age in range(18, 60):
        print "Adults. Your payment is 30$ per month"
        prize = 30
        logger.info('Age, Prize is: {} {}'.format(age, prize))
        return prize

    if age in range(60, 100):
        print "Pensioners. Your payment is 40$ per month"
        prize = 40
        logger.info('Age, Prize is: {} {}'.format(age, prize))
        return prize


if __name__ == "__main__":
    assert count_prize(7) == 10
    assert count_prize(15) == 20
    assert count_prize(22) == 30
    assert count_prize(70) == 40

    assert count_prize(0) == 10
    assert count_prize(12) == 10

    assert count_prize(13) == 20
    assert count_prize(17) == 20

    assert count_prize(18) == 30
    assert count_prize(59) == 30

    assert count_prize(60) == 40
    assert count_prize(99) == 40