#cookToCode
#Created for School
#12/10/2018

#This program will total purchased items, tax if need be, and calculate change

#Variable Dictionary:
#cost           -Cost of an individual item
#totalCost      -The cost of all items 
#finalCost      -The total amount of all items and tax
#tax            -The tax on an indiviudal item if applicable
#totalTax       -The total tax on all taxable items 
#payment        -User inputed payment to the cashier
#change         -The change due to the user
#more           -Variable used to indicate if the user has more items to add
#taxable        -Variable used to indicate if the user's item is taxable

#------------------------------Functions-----------------------------------------------

#This will take the price of the item and return the amount added in tax
def taxFunc():
    tax = cost * .07

    return tax

#This will calculate and print the change given to the user
def changeFunc():
    change = payment - finalCost

    print(f'Your change is ${change:.2f}')

#-----------------------Program Begins----------------------------------
#more starts the loop
more = 'y'
#This sets a spot for the totals to add up
totalTax = float(0.0)
totalCost = float(0.0)
finalCost = float(0.0)

#loop begins
while more == 'y' or more == 'Y':
    taxable = input('If the item is taxable please enter a t for taxable or an n for not taxable.\t:')
    cost = float(input('Enter the price of the item.\t:$'))
    if taxable == 't' or taxable == 'T':
        tax = taxFunc()
        totalTax = tax + totalTax
    totalCost = cost + totalCost
    finalCost = totalCost + totalTax
    more = input('Do you have anymore items to purchase (y/n)?\t:')
#Loop ends
print('\n\n')   #This just adds space

print(f'Cost of items is ${totalCost:.2f}')
print(f'Tax              ${totalTax:.2f}')
print(f'Total            ${finalCost:.2f}')

print('\n\n')   #This just adds space

payment = float(input('How much money are you giving the clerk?\t:$'))
changeFunc()
