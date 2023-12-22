import source_functions

#anything using letters needs to be a string
def main():
    num = input("Enter a number to convert: ")
    base1 = int(input("Enter the base of the original number: "))
    base2 = int(input("Enter the base to convert to: "))
    print("The number is:", source_functions.base_convert_any(base1, base2, num))
    input("Press Enter to exit: ")

'''
syntax:
source_functions.base_convert_any(base_original, base_convert, num)
source_functions.base_convert_to_10(base, num)
source_functions.base_convert_from_10(base, num)
'''

main()
