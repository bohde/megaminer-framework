"""
config.py
Creator: Josh Bohde
Description: Module to parse config
"""

from ConfigParser import SafeConfigParser

def formatAttr(n):
    """
    function formatAttr
    casts an arbitrary string to either an int or float, if it can
    """
    try:
        return int(n)
    except:
        pass
    try:
        return float(n)
    except:
        pass
    return n

def getUserInfo(user, cfgfile):
    """getUserInfo
       returns a dictionary containing the attribute value pairs
       as specified in the given config file, or returns None if no such
       information is present."""
    userInfo = dict()
    cparse = SafeConfigParser()
    cparse.optionxform = str
    cparse.read(cfgfile)
    key = user
    if cparse.has_section(key):
        userInfo = dict([(item[0], str(item[1])) for item in cparse.items(key)])
        if 'screenName' not in userInfo:
            userInfo['screenName'] = user
    else:
        userInfo = None
    return userInfo
