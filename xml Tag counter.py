tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for x in tokens :
    if x[0]=="<":
       count = count + 1

print(count)
