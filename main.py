def hello():
   return("Hello, World!")

print(hello())

name = {'dave'}

def goodbye(name):
    return("Goodbye, {}. We'll miss you!").format(name)

print(goodbye(name))
