def demo_exceptions(testCase):
    try:
        if testCase == 1:
            result = 10 / 0            
            
        elif testCase == 2:
            num = int("Hello")         
            
        # elif testCase == 3:
        #     total = "Age: " + 25       
            
        elif testCase == 4:
            my_list = [10, 20]
            print(my_list[5])       
            
    except ZeroDivisionError:
        print("Caught a ZeroDivisionError: Cannot divide by zero!")
    except ValueError:
        print("Caught a ValueError: Invalid value provided!")
    except TypeError:
        print("Caught a TypeError: Incompatible data types used together!")
    except IndexError:
        print("Caught an IndexError: List index is out of range!")

print("--- Exception Demonstration ---")
demo_exceptions(1)
demo_exceptions(2)
demo_exceptions(3)
demo_exceptions(4)