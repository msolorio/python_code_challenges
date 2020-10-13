def playsBanjo(name):
    if not isinstance(name, str):
        raise TypeError('first parameter must be a string')

    if name[0].lower() == 'r':
        return True

    return False
