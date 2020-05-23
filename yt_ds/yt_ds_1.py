spendings = [2200, 2350, 2600, 2130, 2190]

## In Feb, how many dollars you spent extra compare to January?
print(f'In feb money spent is {spendings[1] - spendings[0]}')

## Find out your total expense in first quarter (first three months) of the year.
print(f'Spending of first quarter is {sum(spendings[0:3])}')

## Find out if you spent exactly 2000 dollars in any month
print(f'Did I spend 2000 dollars in any month: {2000 in spendings}')
## June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
spendings.append(1980)
spendings

## You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
spendings[4] = spendings[3] - 200