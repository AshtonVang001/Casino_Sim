from blackjack.blackJackRules import Rules as BlackjackRules
from roulette.aRoulette import A_Roulette as RouletteRules
from slots.slotRules import SlotsRules
from poker.thPoker import TexasHoldemRules
import random

# unified simulation class
class CasinoSimulation:
    def __init__(self, bankroll):
        self.bankroll = bankroll

        self.blackjack = BlackjackRules(bankroll)
        self.roulette = RouletteRules()
        self.slots = SlotsRules(bankroll)
        self.poker = TexasHoldemRules(bankroll)

    # abstraction of each game
    def play_blackjack(self, bet):
        outcome = random.choices(
            ["win", "lose", "push"]
            #weights=[
            #    self.blackjack.playerP,
            #    self.blackjack.dealerP,
            #    self.blackjack.pushP
            #]
        )[0]

        if outcome == "win":
            return bet
        elif outcome == "lose":
            return -bet
        return 0

    def play_roulette(self, bet):
        return self.roulette.resolve_bet([random.randrange(37)], bet)

    def play_slots(self, bet):
        _, result = self.slots.play(bet)
        return result

    # individual rounds
    def play_round(self):
        bet = min(10, self.bankroll)

        game = random.choice(["blackjack", "roulette", "slots"])

        if game == "blackjack":
            result = self.play_blackjack(bet)

        elif game == "roulette":
            result = self.play_roulette(bet)

        else:
            result = self.play_slots(bet)

        self.bankroll += result
        return game, result, self.bankroll


## MAIN SIMULATION ##
def run_simulation(rounds=1000):
    buy_in = float(input("Enter your buy in: "))
    sim = CasinoSimulation(buy_in)

    for i in range(rounds):
        game, result, bankroll = sim.play_round()

        print(f"{i}: {game} | {result} | bankroll = {bankroll}")

        if bankroll <= 0:
            print("Player is bankrupt")
            break

    print("Final bankroll:", sim.bankroll)


# run it
run_simulation()
