print ('STRING FUNCTIONS:')
print('Placeholder {} ' .format('Arsch'))
print (' String Concat  ' +     '234'  )
print (' Number Concat  ' +     str(234)  )
name ='Eckhard'

print('First Letter', name[0])
print('Length:', len(name))
print(name.upper());
print(name.lower());
print((name +' ') * 5);

version =3
print('I love Python ' + str(version))
print('Ebi {}s {}.' .format('love','Python'))
print('I {0} {1}. {1} {0}s me.' .format('love','Python'))


first = 'I'
second= 'love'
third = 'Perchpike Fishing'
fourth = 2020
print('{} {} {} {}' .format(first, second, third, str(fourth)))


print('Left alignment')
print (' {0:8} | {1:8}'.format('Fruit', 'Quantity'))
print (' {0:8} | {1:8}'.format('Apple', 10))
print (' {0:8} | {1:8}'.format('Banana', 3))

print('Left alignment (Default')
print (' {0:8} | {1:<8}'.format('Fruit', 'Quantity'))
print (' {0:8} | {1:<8}'.format('Apple', 10))
print (' {0:8} | {1:<8}'.format('Banana', 3))

print('Center alignment with decimals')
print (' {0:8} | {1:^8}'.format('Fruit', 'Quantity'))
print (' {0:8} | {1:^8.2f}'.format('Apple', 10))
print (' {0:8} | {1:^8.2f}'.format('Banana', 3))

input = input('Set input: ')
print('Input: {}'  .format(input))
