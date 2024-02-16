print('Earned amount:')
print('Bubblegum: $202')
print('Toffee: $118')
print('Ice cream: $2250')
print('Milk chocolate: $1680')
print('Doughnut: $1075')
print('Pancake: $80\n')
print('Income: $5405.0')
income = 5405
expenses = int(input('Staff expenses:'))
other_expenses = int(input('Other expenses:'))

print('Net income: ',income-(expenses+other_expenses), sep='$')

def second():
    line1 = "Night, square, apothecary, lantern,"
    line2 = "Its meaningless and pallid light."
    line3 = "Return a half a lifetime after – "
    line4 = "All will remain. A scapeless rite."

    # your one print() statement here
    print(line1, line2,line3,line4, sep='\n')


def third():
    word = input()
    numberSpaces = int(input())
    print(*word, sep=' '*numberSpaces)



