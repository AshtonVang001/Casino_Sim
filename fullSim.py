from blackJackRules import Rules as BlackjackRules
from aRoulette import A_Roulette as RouletteRules
from slotRules import SlotsRules
from thPoker import TexasHoldemRules
import random
import matplotlib.pyplot as plt

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
            ["win", "lose", "push"],
            weights=[
                self.blackjack.playerP,
                self.blackjack.dealerP,
                self.blackjack.pushP
            ]
        )[0]

        if outcome == "win":
            return bet
        elif outcome == "lose":
            return -bet
        return 0

    def play_roulette(self, bet):
        return self.roulette.Play([random.randrange(37)], bet)

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

    bankroll_history = [buy_in]
    games_played = []

    for i in range(rounds):
        game, result, bankroll = sim.play_round()
        bankroll_history.append(bankroll)
        games_played.append(game)

        print(f"{i}: {game} | {result} | bankroll = {bankroll}")

        if bankroll <= 0:
            print("Player is bankrupt")
            break

    print("Final bankroll:", sim.bankroll)
    plot_results(bankroll_history, games_played, buy_in)


def plot_results(bankroll_history, games_played, buy_in):
    game_colors = {"blackjack": "#e74c3c", "roulette": "#2ecc71", "slots": "#3498db"}
    rounds = list(range(len(bankroll_history)))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    fig.suptitle("Casino Simulation Results", fontsize=14, fontweight="bold")

    # bankroll over time with scatter points colored by game
    ax1.plot(rounds, bankroll_history, color="gray", linewidth=1, zorder=1)
    ax1.axhline(y=buy_in, color="black", linestyle="--", linewidth=0.8, label=f"Buy-in (${buy_in:.0f})")
    for game, color in game_colors.items():
        idxs = [i + 1 for i, g in enumerate(games_played) if g == game]
        ax1.scatter(idxs, [bankroll_history[i] for i in idxs], color=color, s=8, label=game.capitalize(), zorder=2)
    ax1.set_xlabel("Round")
    ax1.set_ylabel("Bankroll ($)")
    ax1.set_title("Bankroll Over Time")
    ax1.legend(loc="upper right", markerscale=2)

    # pie chart of game frequency
    counts = {g: games_played.count(g) for g in game_colors}
    ax2.pie(
        counts.values(),
        labels=[g.capitalize() for g in counts],
        colors=list(game_colors.values()),
        autopct="%1.1f%%",
        startangle=90,
    )
    ax2.set_title("Game Distribution")

    plt.tight_layout()
    plt.show()


# run it
run_simulation()
