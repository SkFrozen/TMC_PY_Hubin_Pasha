class Soda:
    
    def __init__(self, taste="usual"):
        self.taste = taste
    
    def what_is_taste(self):
        return f"You have a soda with the {self.taste} taste"
    
usual = Soda("strawbarry")

print(usual.what_is_taste())