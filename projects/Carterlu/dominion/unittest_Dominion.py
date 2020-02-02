from unittest import TestCase
import testUtility
import random
from collections import defaultdict
import Dominion

class TestCard(TestCase):


    def setUp(self):
        #data setup
        # Get player names
        self.player_names = testUtility.GetPlayers(random.randint(2, 4))

        self.nC, self.nV = testUtility.SetVicCoin(self.player_names)

        # Define box
        self.box = testUtility.CreateBox(self.nV)

        # setUp supply order
        self.supply_order = testUtility.InitializeSupplyOrder()

        # Pick 10 cards from box to be in the supply.]
        # And set the correct amount of supply for coins and victory cards
        self.supply = testUtility.SetSupply(self.box, self.player_names, self.nV, self.nC)

        # initialize the trash
        self.trash = []

        # Costruct the Player objects
        self.players = testUtility.InitializePlayers(self.player_names)

    def test_init(self):
        self.setUp()

        #setup test variables
        cost = 2
        buypower = 6
        currentName = self.player_names[0]

        # create card with the above variables
        card = Dominion.Coin_card(self.player.name, cost, buypower)

        # confirm the card was created correctly
        self.assertEqual(currentName, card.name)
        self.assertEqual(buypower, card.buypower)
        self.assertEqual(cost, card.cost)
        self.assertEqual("coin", card.category)
        self.assertEqual(0, card.vpoints)
    def test_use(self):
        self.setUp()


    def test_react(self):
       pass
