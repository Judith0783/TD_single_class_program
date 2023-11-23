
from lib.diary_entry import *
import pytest
"""
Given an empty title and contents
Raises an error
"""
def test_errors_on_empty_title():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "my contents")
    assert str(err.value) == "Diary entries must have a title  or content"
    
"""Given an empty title and contents
Raises an error
"""
def test_errors_on_empty_content():
    with pytest.raises(Exception) as err:
        DiaryEntry("my title", "")
    assert str(err.value) == "Diary entries must have a title  or content"
    
""""
Given a tittle and contents
#format returns a formatted entry, like:
"My Title: These are contents"
"""
def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"
    
    """
    Given a title and a contents
    #count words returns the number of words in the title and the contents
    """
def test_counts_words_in_both_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4
    
    """
    Given a wpm of 2
    And a text with 2 words
    #reading_time returns 1 minute
    """
    
def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My Title", "one two")
    result = diary_entry.reading_time(2)
    assert result == 1
    
    """
    Given a wpm of 2
    And a text with 4 words
    #reading_time returns 2 minute
    """
    
def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My Title", "one two three four")
    result = diary_entry.reading_time(2)
    assert result == 2
          
    """
    Given a wpm of 2
    And a text with 4 words
    #reading_time returns 2 minute
    """
    
def  test_reading_time_with_two_wpm_and_three_words():      
    diary_entry = DiaryEntry("My Title", "one two three")
    result = diary_entry.reading_time(2)
    assert result == 2
    
    """
    Given a wpm of 0
    #readind tinme Raises an error 
    """
    
def test_reading_time_wpm_zero():
    diary_entry = DiaryEntry("My Title", "one two three")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "Cannot calculate reading time with wpm of 0"
    
    """
    Given a content of six words
    And a wpm of 2
    And a two minutes of 1
    #reading chunk returns the first four words
    """
    
def test_reading_chunk_with_two_wpm_and_one_minute():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "one two"
    
    """
    Given a content of six words
    And a wpm of 2
    And a two minutes of 2
    #reading chunk returns the first four words
    """
    
def test_reading_chunk_with_two_wpm_and_two_minutes():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"
    
    """
    Given a context of six words
    First time, #reading_chunk(2, 1) returns "one two"
    Next time, #reading_chunk(1, 1) "Three four"
    Next time, #reading_chunk(2, 1) "five six"
    """
    
def test_reading_time_with_two_wpm_and_one_minute_called_multiple_times():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2 ,1) == "one two"
    assert diary_entry.reading_chunk(1 ,1) == "three"
    assert diary_entry.reading_chunk(2 ,1) == "four five"
    
    """
    Given a context of six words
    If #reading-chunk is called repeatedly
    The last chunk is the last words in the text, even if shorter than could be read
    The next chunk after that is at the start again
    """
    
def test_reading_chunk_wraps_around_on_multiple_calls():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2 ,2) == "one two three four"
    assert diary_entry.reading_chunk(2 ,2) == "five six"
    assert diary_entry.reading_chunk(2 ,2) == "one two three four"

    """
    Given a context of six words
    If #reading-chunk is called repeatedly with an exact ending
    The last chunk is the last words in the text, 
    The next chunk after that is at the start again
    """
    
def test_reading_chunk_wraps_around_on_multiple_calls_with_exactly_ending():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    assert diary_entry.reading_chunk(2 ,2) == "one two three four"
    assert diary_entry.reading_chunk(2 ,1) == "five six"
    assert diary_entry.reading_chunk(2 ,2) == "one two three four"

                    