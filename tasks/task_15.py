def id2num(s):
    """ spreadsheet column name to number
    http://stackoverflow.com/questions/7261936

   :param s: str -- spreadsheet column alpha ID (i.e. A, B, ... AA, AB,...)
   :returns: int -- spreadsheet column number (zero-based index)

    >>> id2num('A')
    0
    >>> id2num('B')
    1
    >>> id2num('XFD')
    16383
    >>>

    """
    n = 0
    for ch in s.upper():
        n = n * 26 + (ord(ch) - 65) + 1
    return n - 1

print(id2num('A'))
print(id2num('B'))
print(id2num('AA'))
print(id2num('AB'))
print(id2num('XFD'))