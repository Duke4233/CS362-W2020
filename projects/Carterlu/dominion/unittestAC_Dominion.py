from unittest import TestCase
import testUtility
import random
#from collections import defaultdict
import Dominion

class TestAction_card(TestCase):
    def setUp(self):
        # data setup
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
        #setup variables
        currentName = self.player_names[0]

        name = "chapel"
        cost = 100
        cards = 100
        buys = 100
        coins = 100
        actions = -9

        acard = Dominion.Action_card(name, cost, actions, cards, buys, coins)

        self.assertEqual(name, acard.name)
        self.assertEqual(cards, acard.cards)
        self.assertEqual(cost, acard.cost)
        self.assertEqual(actions, acard.actions)
        self.assertEqual(buys, acard.buys)
        self.assertEqual(coins, acard.coins)


    def test_use(self):
        self.setUp()
        currentName = self.player_names[0]

        name = "chapel"
        cost = 100
        cards = 100
        buys = 100
        coins = 100
        actions = -9

        acard = Dominion.Action_card(name, cost, actions, cards, buys, coins)
        acard.test_use(self, currentName, self.trash)

        self.assertEqual(name, acard.name)
        self.assertEqual(cards, acard.cards)
        self.assertEqual(cost, acard.cost)
        self.assertEqual(actions, acard.actions)
        self.assertEqual(buys, acard.buys)
        self.assertEqual(coins, acard.coins)



        pass

    def test_augment(self):
        self.setUp()
        currentName = self.player_names[0]

        name = "chapel"
        cost = 100
        cards = 100
        buys = 100
        coins = 100
        actions = -9

        acard = Dominion.Action_card(name, cost, actions, cards, buys, coins)
        acard.test_augment(self, self.play)
        pass


