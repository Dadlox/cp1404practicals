def covert_to_fahrenheit(input):
    fahrenheit = input * 9.0 / 5 + 32
    return(fahrenheit)

def convert_to_celcius(input):
    celsius = 5 / 9 * (input - 32)
    return(celsius)


def main():
    output= open('temp_output.txt', 'a')
    with open('temp_input.txt') as file:
        choice = input("(C)elcius or (F)ahrenheit: ").upper()
        if choice == "C":
            for line in file:
                temperature = float(line)
                celcius = convert_to_celcius(temperature)
                print(celcius, file=output)
        elif choice == "F":
            for line in file:
                temperature = float(line)
                fahrenheit = covert_to_fahrenheit(temperature)
                print(fahrenheit, file=output)



main()