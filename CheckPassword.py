def check_password(new_pass):
    lower, upper, digit = 0, 0, 0
    if len(new_pass) > 24:
        print("Password can only be up to 24 characters")
    # Checks the strength of the password
    if len(new_pass) > 7:
        for i in new_pass:
            # counting lowercase chars
            if i.islower():
                lower += 1
            # counting uppercase chars
            elif i.isupper():
                upper += 1
            # counting digits
            elif i.isdigit():
                digit += 1
            # There is an illegal character in the password
            else:
                print("Password contains illegal characters")
                return False
    if lower > 0 and upper > 0 and digit > 0:
        return True
    else:
        print("Password is too easy to guess")
        return False