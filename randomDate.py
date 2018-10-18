#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime 
from random import *
from dateutil.parser import parse

def randomDate(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

if __name__ == '__main__':
    print(randomDate(parse('2000-01-01'),parse('2010-01-01')))

