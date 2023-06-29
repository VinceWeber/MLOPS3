
    
    
    # The simplest function to get the user email (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    return input("Tell me your email: ")

#More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

def get_password_from_input():
    Password = input ("Plesae define a password : ")
    if check_password_all_rules(Password):
        return Password
    else:
        return "Please give a password according to our security rules"


def check_password_all_rules(Passw):
    if check_password_if_has_a_numeric_character(Passw) \
        and check_password_if_has_an_alpha_character(Passw) \
        and check_password_if_is_enought_long(Passw) \
        and check_password_if_has_a_special_character(Passw):

        return True
    else :
        return False


def check_password_if_has_a_numeric_character(Passw):
    for c in Passw:
        if c.isdigit(): 
            return True
    return False

def check_password_if_is_enought_long(Passw):
    if len(Passw)>=8:
        return True
    else:
        return False

def check_password_if_has_an_alpha_character(Passw):
    for c in Passw:
        if c.isalpha(): 
            return True
    return False

def check_password_if_has_a_special_character(Passw):
    for c in Passw:
        if c.isalpha()==False and c.isdigit() == False: 
            return True
    return False

"""
ma_chaine=input ("Plesae define a password : ")
print('Is one numeric character ? -> ' + str(check_password_if_has_a_numeric_character(ma_chaine)))
print('Is one alpha character ? -> ' + str(check_password_if_has_an_alpha_character(ma_chaine)))
print('Is one special character ? -> ' + str(check_password_if_has_a_special_character(ma_chaine)))
print('Is  Lenght > 8  :' + str(check_password_if_is_enought_long(ma_chaine)))
print('Is my password acceptable ? -> ' + str(check_password_all_rules(ma_chaine)))"""


def get_username_from_input():
    Username = input ("Please give a username : ")
    if check_username_all_rules(Username):
        return Username
    else:
        return "Please give a valid username not empty and without spaces"
    

def check_username_all_rules(Username):
    
    if len(Username)!=0 :
        for c in Username:
            if c==" ": 
                return False
    else:
        return False

    return True