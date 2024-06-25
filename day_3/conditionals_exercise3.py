a = 'c'
b = 'b'
c = 'c'

if a < b:
    value_1 = a
elif b < c:
    value_1 = c
else:
    value_1 = b

if c < a:
    value_2 = a
else:
    value_2 = b

if value_2 > value_1:
    c = value_1
    value_2 = value_1
    value_1 = c
else:
    c = value_2
    value_2 = value_1
value_1 = c

print(f'the final values are: ({value_1},{value_2})')