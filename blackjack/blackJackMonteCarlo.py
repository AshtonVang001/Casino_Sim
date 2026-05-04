from blackJackAutoSim import AutoSimulation
import matplotlib.pyplot as plt

SIMULATIONS = 10_000
STARTING_MONEY = 100
GOAL = 200
BET = 10


def run_simulations():
    results = [
        AutoSimulation(starting_money=STARTING_MONEY, goal=GOAL, bet=BET).run()
        for _ in range(SIMULATIONS)
    ]

    wins = sum(1 for r in results if r["reached_goal"])
    losses = SIMULATIONS - wins
    win_rate = wins / SIMULATIONS * 100

    all_hands = [r["hands_played"] for r in results]
    all_balances = [r["final_balance"] for r in results]

    avg_hands = sum(all_hands) / SIMULATIONS
    avg_balance = sum(all_balances) / SIMULATIONS
    min_hands = min(all_hands)
    max_hands = max(all_hands)

    print("=" * 45)
    print("       BLACKJACK MONTE CARLO RESULTS")
    print("=" * 45)
    print(f"  Simulations run:     {SIMULATIONS:>10,}")
    print(f"  Starting balance:    ${STARTING_MONEY:>9,}")
    print(f"  Goal balance:        ${GOAL:>9,}")
    print(f"  Bet per hand:        ${BET:>9,}")
    print("-" * 45)
    print(f"  Times goal reached:  {wins:>10,}  ({win_rate:.1f}%)")
    print(f"  Times busted out:    {losses:>10,}  ({100 - win_rate:.1f}%)")
    print("-" * 45)
    print(f"  Avg hands per game:  {avg_hands:>10.1f}")
    print(f"  Min hands played:    {min_hands:>10,}")
    print(f"  Max hands played:    {max_hands:>10,}")
    print(f"  Avg final balance:   ${avg_balance:>9.2f}")
    print("=" * 45)

    plot_results(wins, losses, win_rate, all_hands, all_balances)


def plot_results(wins, losses, win_rate, all_hands, all_balances):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Blackjack Monte Carlo Results", fontsize=14, fontweight="bold")

    # outcome bar chart
    axes[0].bar(["Goal Reached", "Busted Out"], [wins, losses], color=["#2ecc71", "#e74c3c"])
    axes[0].set_title("Outcomes")
    axes[0].set_ylabel("Simulations")
    for i, v in enumerate([wins, losses]):
        axes[0].text(i, v + 50, f"{v:,}\n({[win_rate, 100 - win_rate][i]:.1f}%)", ha="center", va="bottom")

    # hands played histogram
    axes[1].hist(all_hands, bins=40, color="#3498db", edgecolor="white", linewidth=0.3)
    axes[1].set_title("Hands Played per Simulation")
    axes[1].set_xlabel("Hands")
    axes[1].set_ylabel("Frequency")
    axes[1].axvline(sum(all_hands) / len(all_hands), color="black", linestyle="--", linewidth=1, label=f"Avg: {sum(all_hands)/len(all_hands):.1f}")
    axes[1].legend()

    # final balance histogram
    axes[2].hist(all_balances, bins=20, color="#9b59b6", edgecolor="white", linewidth=0.3)
    axes[2].set_title("Final Balance Distribution")
    axes[2].set_xlabel("Balance ($)")
    axes[2].set_ylabel("Frequency")
    axes[2].axvline(sum(all_balances) / len(all_balances), color="black", linestyle="--", linewidth=1, label=f"Avg: ${sum(all_balances)/len(all_balances):.2f}")
    axes[2].legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_simulations()
