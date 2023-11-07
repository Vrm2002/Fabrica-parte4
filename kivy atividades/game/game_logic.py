from random import randint

class Game_Logic():
    def __init__(self):
        
        pass
        
        
    def number_collector(self, x):
        
        self.user_number = x
        
        
    def random_number_generator(self):
        
        random_number = randint(0,100)
        return random_number
    
    
    def number_confirmer(self,x):
        
        if self.user_number == x:
            return 'Congratulations! You won!'
        
        else:
            if self.user_number > x:
                return 'Lower'
            
            elif self.user_number < x:
                return 'Higher'
        
    
    
        