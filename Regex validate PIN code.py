def validate_pin(pin):
    if pin.isdigit() is True:
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False

pin = "132312"
print(validate_pin(pin))
