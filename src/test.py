import unittest
from blackjack import *
from cards import *
from formatting import *

class TestCard( unittest.TestCase ):
    def setUp( self ):
        self.aceClubs= card.Card(1,card.Clubs)
        self.twoClubs= card.Card(2,card.Clubs)
        self.tenClubs= card.Card(10,card.Clubs)
        self.kingClubs= card.Card(13,card.Clubs)
        self.aceDiamonds= card.Card(1,card.Diamonds)
    def testString( self ):
        self.assertEquals( " AC", str(self.aceClubs) )
        self.assertEquals( " 2C", str(self.twoClubs) )
        self.assertEquals( "10C", str(self.tenClubs) )
    def testOrder( self ):
        self.assertTrue( self.tenClubs < self.kingClubs )
        self.assertFalse( self.tenClubs >= self.kingClubs )
        self.assertTrue( self.kingClubs < self.aceClubs )
        self.assertTrue( self.aceClubs == self.aceDiamonds )

if __name__ == "__main__":
    unittest.main()