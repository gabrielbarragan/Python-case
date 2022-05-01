"""python functions"""

#one function

def one(number: int, rang: list):
    """
    number: any number
    rang: list with min and max value for range of number since min to max[min, max]
    """
    if len(rang) > 2 or len(rang) < 2:
        raise Exception("El rango debe ser una lista con 2 valores (min y max)")
    else:
        min_value= rang[0]
        max_value= rang[1]
        all_range = [num for num in range(min_value,max_value)]
        if number in all_range:
            result = "You are One"
            return result 
        else:
            return False


#second function

def second(number: int, rang: list):
    """
    number: any number
    rang: list with min and max value for range of number since min to max[min, max]
    """
    if len(rang) > 2 or len(rang) < 2:
        raise Exception("El rango debe ser una lista con 2 valores (min y max)")
    else:
        min_value= rang[0]
        max_value= rang[1]
        all_range = [num for num in range(min_value,max_value)]
        if number in all_range:
            result = "You are Second"
            return result
        else:
            return False

#third function

def third(number: int, rang: list):
    """
    number: any number
    rang: list with min and max value for range of number since min to max[min, max]
    """
    if len(rang) > 2 or len(rang) < 2:
        raise Exception("El rango debe ser una lista con 2 valores (min y max)")
    else:
        min_value= rang[0]
        max_value= rang[1]
        all_range = [num for num in range(min_value,max_value)]
        if number in all_range:
            result = "You are Third"
            return result
        else:
            return False

#default function

def default(number: int, rang: list):
    """
    number: any number
    rang: list with min and max value for range of number since min to max[min, max]
    """

    if len(rang) > 2 or len(rang) < 2:
        raise Exception("El rango debe ser una lista con 2 valores (min y max)")
    else:
        min_value= rang[0]
        max_value= rang[1]
        all_range = [num for num in range(min_value,max_value)]
        if number not in all_range:
            result = "You are the best"
            return result
        else:
            return False

#numbers_to_ranges function
def numbers_to_ranges(number):

    my_dict = {
        1: one(number, [0,20]),
        2: second(number, [20,30]),
        3: third(number, [30,40]),
        4: default(number, [0,40]),
    }
 
    print(my_dict)

    
    #switch_example function
    def switch_example(speed, ranges):



        

#driver code

#switch o case con número 37
print(numbers_to_ranges(37) == "You are Third")
#switch o case con número 10
print(numbers_to_ranges(10) == "You are One")
#switch o case con número 25
print(numbers_to_ranges(25) == "You are Second")
#switch o case con número 41
print(numbers_to_ranges(41) == "You are the best")
