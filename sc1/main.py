def feet_to_meters(value):
    return value * 0.3048

feet = float(input('? '))
print(f'{feet}ft = {feet_to_meters(feet)}mt')