import math
import data

def base_convert_any(base_original, base_convert, num):
    #check if the bases are the same
    if(base_original == base_convert):
        return num;

    #call conversion functions
    if(base_original == 10):
        return base_convert_from_10(base_convert, num)
    else:
        num = base_convert_to_10(base_original, num)
        return base_convert_from_10(base_convert, num)

#supports up to base 36
def base_convert_to_10(base, num):
    #validate base
    if (base <= 0 or base >= 37):
        return "invalid base"
    
    #check if the number is a string, if not, make it a string
    if (isinstance(num, int)):
        num = str(num)

    #get position for powers
    position = len(num)

    #have a variable to store the value
    value = 0

    #convert to base 10
    for i in num:
        if (i.upper() in data.MAP_OF_NUMBERS):
            value += data.MAP_OF_NUMBERS[i.upper()] * base**(position-1)
        else:
            value += int(i) * base**(position-1)
        position -= 1
        
    return value

#supports up to base 36
def base_convert_from_10(base, num):
    #validate base
    if (base <= 0 or base >= 37):
        return "invalid base"

    #list is used to keep up with powers
    power_list = []

    #loop until number is converted
    while(num > 0):
        val = int(math.log(num, base))
        power_list.append(int(math.log(num, base)))
        num -= base**val

    #convert power list into the valid number
    return turn_to_num(base, power_list)

def turn_to_num(base, power_list):
    #generate slots for the number
    slots = [0] * (power_list[0]+1)

    #calculates the numebr
    for i in power_list:
        slots[i] += 1

    #get number in correct form
    slots.reverse()

    #turn it into a string
    value = ""
    for i in slots:
        if (i > 9):
            value += data.MAP_OF_LETTERS[i]
        else:
            value += str(i)

    return value
