# Generate MyCustomError
# class MyCustomError(TypeError):
#     def __init__(self, message, code):
#         super().__init__(f'Error code {code}: {message}')
#         self.code = code
        
# raise MyCustomError('OUCH! An Error Happened.', 500)


# Generate RunTimeErrorWithCode     
# class RuntimeErrorWithCode(Exception):
#    """
#    Exception raised when specific error code is needed
#    """ 
#    def __init__(self, message, code):
#         super().__init__(f'Error code {code}: {message}')
#         self.code = code
        
# err = RuntimeErrorWithCode('An Error Happened.', 500)
# print(err.__doc__)


# Example of using Try , Except , Finally Fuction to get the results
def power_of_two():
    user_input = input('Please enter the number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input is invalid. try to default is 0')
        return 0
    finally:
        n_square = n ** 2
        return n_square
    
print(power_of_two())
print(power_of_two())