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

def configWeapons(cfgfile):
        """
        function configWeapons
        reads the config file, parses it, making each section a weapon.
        """
        weapons = dict()
        cparse = SafeConfigParser()
        cparse.optionxform = str
        cparse.read(cfgfile)
        for key in cparse.sections():
            weapons[key] = dict([(item[0], formatAttr(item[1])) for item in cparse.items(key)])
        return weapons

def configClassDefaults(mainDict, cfgfile):
    """
    Pass in the namespace and the config file.
    Iterates over the namespace, assigning values.
    """
    cparse = SafeConfigParser()
    cparse.optionxform = str
    cparse.read(cfgfile)
    for k, v in mainDict.iteritems():
        if cparse.has_section(k):
            v.__dict__.update(dict([(item[0], formatAttr(item[1])) for item in cparse.items(k)]))

def configHuman(human, cfgfile):
    """
    function configHuman
    searches the config file for the human's weapon, then modifies the 
    human's stats as specified in the config file.
    """
    cparse = SafeConfigParser()
    cparse.optionxform = str
    cparse.read(cfgfile)
    if cparse.has_section(human.weapon.desc):
        for item in cparse.items(human.weapon.desc):
            setattr(human, item[0], formatAttr(item[1]))

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

if __name__ == "__main__":
   #print configWeapons('config/weapons.cfg')
   print getUserInfo("Shell AI", 'config/login.cfg')
