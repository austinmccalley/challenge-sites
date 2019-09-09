def validate_pin(pin):

    if pin.isdigit() and (len(str(pin)) == 4 or len(str(pin)) == 6):
        return True
    else:
        return False;