# -*-coding: utf-8 -*-

import functools


def timer(func):
    """
    计时器
    @param {function} func
    """
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        start = datetime.datetime.now()
        f = func(*args, **kwargs)
        end = datetime.datetime.now()
        print (u'Function {} spend {} seconds.'.format(func.__name__, (end-start).total_seconds()))
        return f
    return decorator