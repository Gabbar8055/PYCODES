names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for x in names:
  usernames.append(x.lower().replace(" ", "_"))

print(usernames)
