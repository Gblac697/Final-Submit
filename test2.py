from CP_Project import *
from Stat_Sheet import *
import unittest
from unittest.mock import patch
from io import StringIO

print("This game is great and works :)")   
class TestAdventureGame(unittest.TestCase):
    
    def setUp(self):
        # Set up a fresh player for each test case
        self.player = chara_trait(100, 10)

    @patch('CP_Project.input', create=True)
    @patch('sys.stdout', new_callable=StringIO)
    def test_successful_gameplay1(self, mock_stdout, mock_input):
        # Add enough inputs to ensure the game completes or reaches a terminal point
        mock_input.side_effect = ['start','north', 'grab rope', 'go to lake', 'throw rope', 'sail home', 'no', 'stop playing']

        # Run the function, capturing printed output
        player_spawn(self.player)

        # Retrieve printed output from the mock_stdout
        output = mock_stdout.getvalue()

        self.assertIn("Thanks for Playing", output, "test pass")
            
if __name__ == "__main__":
    try:
        unittest.main()
    except Exception as e:
        print(f"Error running tests: {e}")

    
  
    


    
