def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

# With only a name argument 
greet("Tim")

# With name and custom greeting
greet(name="Tim", greeting="Good Morning")

# With greeting passed as a keyword argument 
greet(name="Tim", greeting="Hello")

