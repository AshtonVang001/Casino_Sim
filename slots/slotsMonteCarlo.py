import matplotlib.pyplot as plt
from slotsAutoSim import AutoSimulation

SIMULATIONS = 10_000
STARTING_MONEY = 100
GOAL = 200
BET = 10


def run_simulations():
    moneyHist = [[]]
    results = [[]]
    results = [
        AutoSimulation(i, starting_money=STARTING_MONEY, goal=GOAL, bet=BET).run()
        for i in range(SIMULATIONS)
    ]
    #i know this is gross but I'm desperate. I need SOME data for the graph, i don't care if it's right...
    moneyHist = [
        AutoSimulation(i, starting_money=STARTING_MONEY, goal=GOAL, bet=BET).moneyHistory()
        for i in range(SIMULATIONS)
    ]
    
    wins = sum(1 for r in results if r["reached_goal"])
    losses = SIMULATIONS - wins
    win_rate = wins / SIMULATIONS * 100

    all_rounds = [r["rounds_played"] for r in results]
    all_balances = [r["final_balance"] for r in results]

    avg_rounds = sum(all_rounds) / SIMULATIONS
    avg_balance = sum(all_balances) / SIMULATIONS
    min_rounds = min(all_rounds)
    max_rounds = max(all_rounds)

    print("=" * 45)
    print("         SLOTS MONTE CARLO RESULTS")
    print("=" * 45)
    print(f"  Simulations run:     {SIMULATIONS:>10,}")
    print(f"  Starting balance:    ${STARTING_MONEY:>9,}")
    print(f"  Goal balance:        ${GOAL:>9,}")
    print(f"  Bet per round:       ${BET:>9,}")
    print("-" * 45)
    print(f"  Times goal reached:  {wins:>10,}  ({win_rate:.1f}%)")
    print(f"  Times busted out:    {losses:>10,}  ({100 - win_rate:.1f}%)")
    print("-" * 45)
    print(f"  Avg rounds per game: {avg_rounds:>10.1f}")
    print(f"  Min rounds played:   {min_rounds:>10,}")
    print(f"  Max rounds played:   {max_rounds:>10,}")
    print(f"  Avg final balance:   ${avg_balance:>9.2f}")
    print("=" * 45)

    plt.title("10 Player Bank Accounts")
    plt.ylabel("Money")
    plt.xlabel("Rounds")
    x = []           

    print(AutoSimulation(10, starting_money=STARTING_MONEY, goal=GOAL, bet=BET).moneyHistory())

    for _, run in enumerate(moneyHist):
        x = range(len(run))
        plt.plot(x, run, alpha = .7, linewidth=1)
    plt.show()

if __name__ == "__main__":
    run_simulations()
