#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The cat must have slept on the keyboard!!!

Strip this terribly formatted string of its excess characters.
"""


NERVOUS_AS = """




 //////////A long-tailed cat in a room full of rockin' chairs.,,,,,,,,,, 





"""

NERVOUS_AS = NERVOUS_AS.strip()

NERVOUS_AS = NERVOUS_AS.rstrip(',')

NERVOUS_AS = NERVOUS_AS.lstrip('/')

print NERVOUS_AS
