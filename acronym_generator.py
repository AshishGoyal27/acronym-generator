expression = input("Enter an expression")
my_list = expression.split()

s = ""
for word in my_list:
  s = s + word[0].upper()
print(s)
