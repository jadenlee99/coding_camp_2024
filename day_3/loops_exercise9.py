mylist = ['calculation',
          'tree',
          'density',
          'soccer',
          'cat',
          'turtle',
          'supercalifragilisticexpialidocious']

new_list = []

for i in range(len(mylist)):
    if 'a' not in mylist[i]:
        new_list.append(mylist[i])

print(new_list)
