from lib.grammar_stats import *

"""
check an string 
If string begings with a capital letter and end with sentence-ending puntuaction mark returns true
otherwise return false
"""
def test_check_text_start_with_capital_letter_and_ending_with_puntuaction_mark():
    grammar_stats = GrammarStats()
    text = "Hello, this is a great day to start with a coffee!, lets start to work.Should we?"
    result = grammar_stats.check(text)
    
    assert result == True
    
    """
    returns the percentage of text passed on the check method
    return and integer with percentage
    """
    
def test_percentage_text_passed_in_check_method():
    grammar_stats = GrammarStats()
    text = "Hello, this is a great day to start with a coffee!, lets start to work. Should we?"
    for txt in [text]:
        result = grammar_stats.check(text)
        
    expected_percentage = 55
    calculated_percentage = grammar_stats.percentage_good()
    assert calculated_percentage == expected_percentage
