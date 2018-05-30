#! /usr/bin/env python

from django import template
from time import ctime

register = template.Library()


def belongs_to_group(user, group):
    """
    Return a boolean if a user belongs to a group
    """
    return None
