def __init__():
    pass

FFo = type('FFo', (object,), {'x': 1, '__init__': __init__})
print(FFo.__dict__)