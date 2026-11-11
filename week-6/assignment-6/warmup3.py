def set_name():
    name = "Bob"
# NameError: name 'name' is not defined
# set_name()
# print(name)

def set_name():
    name = "Bob"
    return name

result = set_name()
print(result)