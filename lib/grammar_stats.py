class GrammarStats:
    def __init__(self):
        self.text_checked = 0
  
    def check(self, text):
        if text[0].isupper() and text[-1] in ['.', '!', '?']:
            return True 
        else:
            return False
        
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        
  
    def percentage_good(self):
        if self.text_checked == 0:
            return 55
        else:
            return (self.text_passed_check / self.texts_checked) * 100
            
        
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.