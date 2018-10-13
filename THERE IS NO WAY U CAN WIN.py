items = {"a","b","c","d","e","f","g","h","i","j","k","l","m"}
take = int(input("take 1,2 or 3 items "))
if take == 1 :
    items.pop()
elif take == 2:
    items.pop()
    items.pop()
elif take == 3:
    items.pop()
    items.pop()
    items.pop()
if take > 3 or take < 0 :
    print("U LOSE")
print(items)
if len(items) == 0 :
    print ("U LOSE")
comp_take = (4 - take)
if comp_take == 1:
    items.pop()
if comp_take == 2:
    items.pop()
    items.pop() 
if comp_take == 3:
    items.pop()
    items.pop()
    items.pop()
print(items)
if len(items) == 0 :
    print ("U WIN")
takei = int(input("take 1,2 or 3 items "))
if takei == 1 :
    items.pop()
elif takei == 2:
    items.pop()
    items.pop()
elif takei == 3:
    items.pop()
    items.pop()
    items.pop()
print(items)
if takei > 3 or takei < 0 :
    print("U LOSE")
if len(items) == 0 :
    print ("U LOSE")
comp_takei = (4 - takei)
if comp_takei == 1:
    items.pop()
if comp_takei == 2:
    items.pop()
    items.pop() 
if comp_takei == 3:
    items.pop()
    items.pop()
    items.pop()
print(items)
if len(items) == 0 :
    print ("U WIN")
takeii = int(input("take 1,2 or 3 items "))
if takeii == 1 :
    items.pop()
elif takeii == 2:
    items.pop()
    items.pop()
elif takeii == 3:
    items.pop()
    items.pop()
    items.pop()
print(items)
if takeii > 3 or takeii < 0 :
    print("U LOSE")
if len(items) == 0 :
    print ("U LOSE")
comp_takeii = (4 - takeii)
if comp_takeii == 1:
    items.pop()
if comp_takeii == 2:
    items.pop()
    items.pop() 
if comp_takeii == 3:
    items.pop()
    items.pop()
    items.pop()
print(items)
if len(items) == 0 :
    print ("U WIN")
takeiii = int(input("take 1,2 or 3 items"))
if takeiii == 1:
    items.pop()
if takeiii == 2:
    print("INVALID NUMBERS OF ITEMS ARE ENTERED AS ONLY 1 ITEM LEFT SO ACCEPT IT :: U LOSE ::")
if takeiii == 3:
    print("INVALID NUMBERS OF ITEMS ARE ENTERED AS ONLY 1 ITEM LEFT SO ACCEPT IT :: U LOSE ::")
if len(items) == 0 :
    print ("U LOSE")
if takeiii > 3 or takeiii < 0 :
    print("U LOSE")