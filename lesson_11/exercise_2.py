class Math:
    
    def addition(self,digit_1, digit_2):
        return f"{digit_1} + {digit_2} = {digit_1 + digit_2}"
    
    def subtraction(self,digit_1, digit_2):
        return f"{digit_1} - {digit_2} = {digit_1 - digit_2}"

    def multiplication(self,digit_1, digit_2):
        return f"{digit_1} * {digit_2} = {digit_1 * digit_2:.2f}"

    def division(self,digit_1, digit_2):
        return f"{digit_1} / {digit_2} = {digit_1 / digit_2:.2f}"
    
action = Math()
print(action.subtraction(17, 177))