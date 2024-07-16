def printHello(who, line_ending='!', count=1):
    for _ in range(count):
        str_line = who + line_ending
        print('Hello, ' + str_line)


variable = 'Tima'

printHello(variable, '!!!', 5)
