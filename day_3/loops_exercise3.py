mydict = {'avocado':'1.99$',
          'bell pepper':'0.89$',
          'strawberries':'2.77$',
          'lemon':'0.89$',
          'blueberries':'7.99$',
          'watermelon':'5.99$',
          'peach':'1.85$'}

budget = '100$'
item = 'lemon'
 
budget = float(budget.strip('$'))
item = float(mydict[item].strip('$'))

remaining_budget = budget
count = 0

while remaining_budget >= item:
    remaining_budget -= item
    count += 1

final_message = f'Units of the specific item is {count} and the remaining budget is {remaining_budget}' # you also need to write code for getting this message properly
print(final_message)