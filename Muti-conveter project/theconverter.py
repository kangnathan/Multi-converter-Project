print("THE ULTIMATE CONVERTER")

def get_exchange_rates():
    exchange_rates = {
        'USD_to_PHP': 55.00,
        'YEN_to_PHP': 0.40,
        'WON_to_PHP': 0.044,
        'PHP_to_USD': 1/55.00,
        'PHP_to_YEN': 1/0.40,
        'PHP_to_WON': 1/0.044
    }
    return exchange_rates

def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates()
    key = f'{from_currency}_to_{to_currency}'
    if key in rates:
        return amount * rates[key]
    else:
        return "Currency conversion not supported"

def convert_length(value, from_unit, to_unit):
    length_conversion_factors = {
        'mm_to_cm': 0.1,
        'mm_to_mtr': 0.001,
        'mm_to_km': 0.000001,
        'cm_to_mm': 10,
        'cm_to_mtr': 0.01,
        'cm_to_km': 0.00001,
        'mtr_to_mm': 1000,
        'mtr_to_cm': 100,
        'mtr_to_km': 0.001,
        'km_to_mm': 1000000,
        'km_to_cm': 100000,
        'km_to_mtr': 1000
    }
    key = f'{from_unit}_to_{to_unit}'
    if key in length_conversion_factors:
        return value * length_conversion_factors[key]
    else:
        return "Length conversion not supported"

def convert_time(value, from_unit, to_unit):
    time_conversion_factors = {
        'sec_to_min': 1/60,
        'sec_to_hr': 1/3600,
        'min_to_hr': 1/60,
        'min_to_sec': 60,
        'hr_to_sec': 3600,
        'hr_to_min': 60
    }
    key = f'{from_unit}_to_{to_unit}'
    if key in time_conversion_factors:
        return value * time_conversion_factors[key]
    else:
        return "Time conversion not supported"

def convert_data_storage(value, from_unit, to_unit):
    data_storage_conversion_factors = {
        'kb_to_mb': 1/1024,
        'kb_to_gb': 1/1048576,
        'kb_to_tb': 1/1073741824,
        'mb_to_kb': 1024,
        'mb_to_gb': 1/1024,
        'mb_to_tb': 1/1048576,
        'gb_to_kb': 1048576,
        'gb_to_mb': 1024,
        'gb_to_tb': 1/1024,
        'tb_to_kb': 1073741824,
        'tb_to_mb': 1048576,
        'tb_to_gb': 1024
    }
    key = f'{from_unit}_to_{to_unit}'
    if key in data_storage_conversion_factors:
        return value * data_storage_conversion_factors[key]
    else:
        return "Data storage conversion not supported"

def main():
    while True:
        try:
            print("\nChoose a conversion type:")
            print("1 - Currency Conversion")
            print("2 - Length Conversion")
            print("3 - Time Conversion")
            print("4 - Data Storage Conversion")
            print("5 - Exit")
            
            choice = input("Enter your choice: ")

            if choice == '1':
                print("\nChoose a currency conversion type:")
                print("1 - USD to PHP")
                print("2 - YEN to PHP")
                print("3 - WON to PHP")
                print("4 - PHP to USD")
                print("5 - PHP to YEN")
                print("6 - PHP to WON")

                currency_choice = input("Enter your choice: ")
                if currency_choice not in ['1', '2', '3', '4', '5', '6']:
                    print("Invalid choice. Please try again.")
                    continue

                currency_amount = float(input("Enter the amount: "))
                currency_units = {
                    '1': ('USD', 'PHP'),
                    '2': ('YEN', 'PHP'),
                    '3': ('WON', 'PHP'),
                    '4': ('PHP', 'USD'),
                    '5': ('PHP', 'YEN'),
                    '6': ('PHP', 'WON')
                }

                from_currency, to_currency = currency_units[currency_choice]
                converted_amount = convert_currency(currency_amount, from_currency, to_currency)
                print("")
                print(f'{currency_amount} {from_currency} is {round(converted_amount, 2)} {to_currency}')

            elif choice == '2':
                print("\nChoose a length conversion type:")
                print("1 - mm to cm")
                print("2 - mm to mtr")
                print("3 - mm to km")
                print("4 - cm to mm")
                print("5 - cm to mtr")
                print("6 - cm to km")
                print("7 - mtr to mm")
                print("8 - mtr to cm")
                print("9 - mtr to km")
                print("10 - km to mm")
                print("11 - km to cm")
                print("12 - km to mtr")
                
                length_choice = input("Enter your choice: ")
                if length_choice not in [str(i) for i in range(1, 13)]:
                    print("Invalid choice. Please try again.")
                    continue

                length_value = float(input("Enter the value: "))
                length_units = {
                    '1': ('mm', 'cm'),
                    '2': ('mm', 'mtr'),
                    '3': ('mm', 'km'),
                    '4': ('cm', 'mm'),
                    '5': ('cm', 'mtr'),
                    '6': ('cm', 'km'),
                    '7': ('mtr', 'mm'),
                    '8': ('mtr', 'cm'),
                    '9': ('mtr', 'km'),
                    '10': ('km', 'mm'),
                    '11': ('km', 'cm'),
                    '12': ('km', 'mtr')
                }

                from_unit, to_unit = length_units[length_choice]
                converted_length = convert_length(length_value, from_unit, to_unit)
                print("")
                print(f'{length_value} {from_unit} is {round(converted_length, 2)} {to_unit}')

            elif choice == '3':
                print("\nChoose a time conversion type:")
                print("1 - sec to min")
                print("2 - sec to hr")
                print("3 - min to hr")
                print("4 - min to sec")
                print("5 - hr to sec")
                print("6 - hr to min")

                time_choice = input("Enter your choice: ")
                if time_choice not in ['1', '2', '3', '4', '5', '6']:
                    print("Invalid choice. Please try again.")
                    continue

                time_value = float(input("Enter the value: "))
                time_units = {
                    '1': ('sec', 'min'),
                    '2': ('sec', 'hr'),
                    '3': ('min', 'hr'),
                    '4': ('min', 'sec'),
                    '5': ('hr', 'sec'),
                    '6': ('hr', 'min')
                }

                from_unit, to_unit = time_units[time_choice]
                converted_time = convert_time(time_value, from_unit, to_unit)
                print("")
                print(f'{time_value} {from_unit} is {round(converted_time, 2)} {to_unit}')

            elif choice == '4':
                print("\nChoose a data storage conversion type:")
                print("1 - kb to mb")
                print("2 - kb to gb")
                print("3 - kb to tb")
                print("4 - mb to kb")
                print("5 - mb to gb")
                print("6 - mb to tb")
                print("7 - gb to kb")
                print("8 - gb to mb")
                print("9 - gb to tb")
                print("10 - tb to kb")
                print("11 - tb to mb")
                print("12 - tb to gb")

                data_storage_choice = input("Enter your choice: ")
                if data_storage_choice not in [str(i) for i in range(1, 13)]:
                    print("Invalid choice. Please try again.")
                    continue

                data_storage_value = float(input("Enter the value: "))
                data_storage_units = {
                    '1': ('kb', 'mb'),
                    '2': ('kb', 'gb'),
                    '3': ('kb', 'tb'),
                    '4': ('mb', 'kb'),
                    '5': ('mb', 'gb'),
                    '6': ('mb', 'tb'),
                    '7': ('gb', 'kb'),
                    '8': ('gb', 'mb'),
                    '9': ('gb', 'tb'),
                    '10': ('tb', 'kb'),
                    '11': ('tb', 'mb'),
                    '12': ('tb', 'gb')
                }

                from_unit, to_unit = data_storage_units[data_storage_choice]
                converted_data_storage = convert_data_storage(data_storage_value, from_unit, to_unit)
                print("")
                print(f'{data_storage_value} {from_unit} is {round(converted_data_storage, 2)} {to_unit}')

            elif choice == '5':
                print("")
                print("Exiting...")
                print("")
                break

            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
