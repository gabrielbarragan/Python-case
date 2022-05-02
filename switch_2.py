"""python functions"""

#one function

def one():

    result = "You are One"
    return result 

#second function
def second():
    
    result = "You are Second"
    return result

#third function
def third():

    result = "You are Third"
    return result

#default function
def default():
   
    result = "You are the best"
    return result

#numbers_to_ranges function
def numbers_to_ranges(number):
    rango_1 = range(0,20)
    rango_2 = range(20,30)
    rango_3 = range(30,40)
    rango_4 = range(0,40)
    ranges_list = [rango_1,rango_2,rango_3, rango_4]

    #switch_example function
    def switch_example(speed, ranges):
        ranges_to_str = {
        one(): speed in ranges[0],
        second(): speed in ranges[1],
        third(): speed in ranges[2],
        default(): speed not in ranges[3],
    }
        
        for key, value in ranges_to_str.items():
            if value == True:
                result = key
        return result

    return switch_example(number,ranges_list)

        

#driver code

#switch o case con número 37

print(numbers_to_ranges(37) == "You are Third")
#switch o case con número 10
print(numbers_to_ranges(10) == "You are One")
#switch o case con número 25
print(numbers_to_ranges(25) == "You are Second")
#switch o case con número 41
print(numbers_to_ranges(41) == "You are the best")
