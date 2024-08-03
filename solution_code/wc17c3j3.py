#Uncrackable wc17c3j3

def chk_len(passwd: str) ->bool:
    """Checks whether the password is having more than 
    8 characters or not"""
    if len(passwd) >= 8 and len(passwd) <= 12:
        return True
    else:
        return False

assert chk_len('travl') is False
assert chk_len('travl5658t77') is True

def has_upper(passwd: str) ->bool:
    i = 0
    for char in passwd:
        if char.isupper():
            i = i + 1
    if i >= 2:
        return True
    else:
        return False 

assert(has_upper('leMEgo')) == True
assert(has_upper('lego')) == False

def has_lower(passwd: str) ->bool:
    i = 0
    for char in passwd:
        if char.islower():
            i = i + 1
    if i >= 3:
        return True
    else:
        return False

assert(has_lower('leMEgo')) == True
assert(has_lower('LEGO')) == False

def has_number(passwd: str) ->bool:
    i = 0
    for char in passwd:
        if char.isnumeric():
            i = i + 1
    if i >= 1:
        return True    
    else:
        return False

assert(has_number('leMEgo')) == False
assert(has_number('LE1O')) == True


def has_what(passwd: str) ->str:
    """Checks the password and returns what it contains, 
    number, alphabets or Spl characters"""
    if chk_len(passwd):
        if has_lower(passwd) and has_upper(passwd) and has_number(passwd):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")

password = input("")

has_what(password)