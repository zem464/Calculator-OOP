# Interface for 3-inputs

# Create class
class input3:
    def operations_display_for3(self):
        # Show operations
        print("\n\033[33;40m\033[1mIn selecting operations, pick a number.\033[0m")
        print("5. +, +\n6. +, -\n7. +, *\n8. +, /\n9. -, +\n10. -, -")
        print("11. -, *\n12. -, /\n13. *, +\n14. *, -\n15. *, *\n16. *, /")
        print("17. /, +\n18. /, -\n19. /, *\n20. /, /")

    def print_add_add(self, add_add):
        print("=", str(add_add))
    
    def print_add_sub(self, add_sub):
        print("=", str(add_sub))
    
    def print_add_multi(self, add_multi):
        print("=", str(add_multi))
    
    def print_add_div(self, add_div):
        print("=", str(add_div))
    
    def print_sub_add(self, sub_add):
        print("=", str(sub_add))
    
    def print_sub_sub(self, sub_sub):
        print("=", str(sub_sub))
    
    def print_sub_multi(self, sub_multi):
        print("=", str(sub_multi))
    
    def print_sub_div(self, sub_div):
        print("=", str(sub_div))

    def print_multi_add(self, multi_add):
        print("=", str(multi_add))
    
    def print_multi_sub(self, multi_sub):
        print("=", str(multi_sub))
    
    def print_multi_multi(self, multi_multi):
        print("=", str(multi_multi))
    
    def print_multi_div(self, multi_div):
        print("=", str(multi_div))
    
    def print_div_add(self, div_add):
        print("=", str(div_add))
    
    def print_div_sub(self, div_sub):
        print("=", str(div_sub))
    
    def print_div_multi(self, div_multi):
        print("=", str(div_multi))
    
    def print_div_div(self, div_div):
        print("=", str(div_div))

    def not_an_option2(self):
        print("\033[31m\033[1mPick only from 5 to 20")