def convert_length(value, from_unit, to_unit):
    conversions = {
        ('cm', 'm'): value / 100,
        ('cm', 'mm'): value * 10,
        ('m', 'cm'): value * 100,
        ('m', 'mm'): value * 1000,
        ('mm', 'cm'): value / 10,
        ('mm', 'm'): value / 1000
    }
    return conversions.get((from_unit, to_unit), value)

def convert_weight(value, from_unit, to_unit):
    conversions = {
        ('g', 'kg'): value / 1000,
        ('g', 'mg'): value * 1000,
        ('kg', 'g'): value * 1000,
        ('kg', 'mg'): value * 1000000,
        ('mg', 'g'): value / 1000,
        ('mg', 'kg'): value / 1000000
    }
    return conversions.get((from_unit, to_unit), value)

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    else:
        return value

def menu():
    while True:
        print('Options:')
        print('Enter "length" for length conversion')
        print('Enter "weight" for weight conversion')
        print('Enter "temperature" for temperature conversion')
        print('Enter "quit" to end the program')
        user_input = input(': ')

        if user_input == 'quit':
            break
        elif user_input == 'length':
            try:
                value = float(input('Enter value: '))
                from_unit = input('Enter from unit (cm, m, mm): ')
                to_unit = input('Enter to unit (cm, m, mm): ')
                if from_unit not in ['cm', 'm', 'mm'] or to_unit not in ['cm', 'm', 'mm']:
                    print('Invalid length units. Please use cm, m, or mm.')
                    continue
                print('Result: {:.2f}'.format(convert_length(value, from_unit, to_unit)))
            except ValueError:
                print('Please enter a valid number.')
        elif user_input == 'weight':
            try:
                value = float(input('Enter value: '))
                from_unit = input('Enter from unit (g, kg, mg): ')
                to_unit = input('Enter to unit (g, kg, mg): ')
                if from_unit not in ['g', 'kg', 'mg'] or to_unit not in ['g', 'kg', 'mg']:
                    print('Invalid weight units. Please use g, kg, or mg.')
                    continue
                print('Result: {:.2f}'.format(convert_weight(value, from_unit, to_unit)))
            except ValueError:
                print('Please enter a valid number.')
        elif user_input == 'temperature':
            try:
                value = float(input('Enter value: '))
                from_unit = input('Enter from unit (celsius, fahrenheit, kelvin): ')
                to_unit = input('Enter to unit (celsius, fahrenheit, kelvin): ')
                if from_unit not in ['celsius', 'fahrenheit', 'kelvin'] or to_unit not in ['celsius', 'fahrenheit', 'kelvin']:
                    print('Invalid temperature units. Please use celsius, fahrenheit, or kelvin.')
                    continue
                print('Result: {:.2f}'.format(convert_temperature(value, from_unit, to_unit)))
            except ValueError:
                print('Please enter a valid number.')
        else:
            print('Invalid input. Please try again.')

# Llama a la función del menú para iniciar el programa
menu()