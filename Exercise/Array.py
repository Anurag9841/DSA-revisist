''' 1. Let us say your expense for every month are listed below,
        January - 2200
        February - 2350
        March - 2600
        April - 2130
        May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this '''

Expense = [2200,2350,2600,2130,2190] # creating a list of expense for every month
''' Question 1 '''
Extra_Spent_Feb = Expense[1] - Expense[0]
print("Extra money spent in feb compared to jan is",Extra_Spent_Feb)

''' Question 2 '''
total = 0
for i in range(0,3):
    total = total + Expense[i]

print('Total Expense in first quarter of year is',total)

''' Question 3 '''

print('Did I spent 2000$ in any month?',2000 in Expense)

''' Question 4 '''

Expense.append(1980)
print('updated expense is',Expense)

''' Question 5 '''

Expense[3] = 1930
print('updated expense is',Expense)


'''2. You have a list of your favourite marvel super heros.'''

heros = ['spider man','thor','hulk','iron man','captain america']

''' Question 1 '''

print('Length of list is ',len(heros))

''' Question 2 '''

print('List after adding black panther is ', heros.append('black panther'))

''' Question 3 '''
heros.remove('black panther')
heros.insert(3,'black panther')

''' Question 4 '''
heros[1:3] = ['doctor strange']
print(heros)

''' Question 5 '''
heros.sort()
print('The sorted list is',heros)


'''3. Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function'''

max_number = int(input('Enter the number'))
odd_number = []
for i in range(1, max_number+1):
    if i%2 !=0:
        odd_number.append(i)

print(odd_number)




