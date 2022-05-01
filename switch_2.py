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



    ranges_to_str = {
        range(0,20): one(),
        range(20,30): second(),
        range(30,40): third(),
        41 :default()
    }
    for key in ranges_to_str.keys():
        
        print(number in key)
            
    #switch_example function
    #def switch_example(speed, ranges):

        

#driver code

#switch o case con número 37
print(numbers_to_ranges(37) == "You are Third")
#switch o case con número 10
print(numbers_to_ranges(10) == "You are One")
#switch o case con número 25
print(numbers_to_ranges(25) == "You are Second")
#switch o case con número 41
print(numbers_to_ranges(41) == "You are the best")
