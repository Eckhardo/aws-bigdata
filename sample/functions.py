def sayHello (name= 'Nobody'):
    print('Hello {}' .format(name))

sayHello()
sayHello('Eberhard')


def sayGoodMorning(first, last):

    """ Say Good Morning """
    print('Hello {} {}' .format(first,last))
    

sayGoodMorning('Ebi', 'Kirsche')


sayGoodMorning(last= 'Ebi', first='Kirsche')

""" help gives a description of your function  """
help(sayGoodMorning)

print(True);
