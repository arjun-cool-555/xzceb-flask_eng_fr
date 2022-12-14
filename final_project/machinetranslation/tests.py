import unittest

from translator import english_to_french,french_to_english

class Test_english_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(""),"") # test when empty is given as input the output is empty.
        self.assertEqual(english_to_french('Hello'),'Bonjour')  # test when 'Hello' is given as input the output is 'Banjour'.
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(""),"") # test when empty is given as input the output is empty.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.
        
unittest.main()