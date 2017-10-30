from pip._vendor.appdirs import unicode


def toUnicode(str):
    res = str.encode('unicode')
    print(res)
    return res

unicode