# Import parent class
from Calcu_Class import calculator

# Create the class method
class more_ope(calculator):
    def add_add(self, inp_num1, inp_num2, inp_num3):
        add_add = inp_num1 + inp_num2 + inp_num3
        return add_add
    
    def add_sub(self, inp_num1, inp_num2, inp_num3):
        add_sub = inp_num1 + inp_num2 - inp_num3
        return add_sub
    
    def add_multi(self, inp_num1, inp_num2, inp_num3):
        add_multi = inp_num1 + inp_num2 * inp_num3
        return add_multi

    def add_div(self, inp_num1, inp_num2, inp_num3):
        add_div = inp_num1 + inp_num2 / inp_num3
        return add_div
    
    def sub_add(self, inp_num1, inp_num2, inp_num3):
        sub_add = inp_num1 - inp_num2 + inp_num3
        return sub_add

    def sub_sub(self, inp_num1, inp_num2, inp_num3):
        sub_sub = inp_num1 - inp_num2 - inp_num3
        return sub_sub
    
    def sub_multi(self, inp_num1, inp_num2, inp_num3):
        sub_multi = inp_num1 - inp_num2 * inp_num3
        return sub_multi

    def sub_div(self, inp_num1, inp_num2, inp_num3):
        sub_div = inp_num1 - inp_num2 / inp_num3
        return sub_div
    
    def multi_add(self, inp_num1, inp_num2, inp_num3):
        multi_add = inp_num1 * inp_num2 + inp_num3
        return multi_add

    def multi_sub(self, inp_num1, inp_num2, inp_num3):
        multi_sub = inp_num1 * inp_num2 - inp_num3
        return multi_sub
    
    def multi_multi(self, inp_num1, inp_num2, inp_num3):
        multi_multi = inp_num1 * inp_num2 * inp_num3
        return multi_multi

    def multi_div(self, inp_num1, inp_num2, inp_num3):
        multi_div = inp_num1 * inp_num2 / inp_num3
        return multi_div
    
    def div_add(self, inp_num1, inp_num2, inp_num3):
        div_add = inp_num1 / inp_num2 + inp_num3
        return div_add

    def div_sub(self, inp_num1, inp_num2, inp_num3):
        div_sub = inp_num1 / inp_num2 - inp_num3
        return div_sub
    
    def div_multi(self, inp_num1, inp_num2, inp_num3):
        div_multi = inp_num1 / inp_num2 * inp_num3
        return div_multi

    def div_div(self, inp_num1, inp_num2, inp_num3):
        div_div = inp_num1 / inp_num2 / inp_num3
        return div_div