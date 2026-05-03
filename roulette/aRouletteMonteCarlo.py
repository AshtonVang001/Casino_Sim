from aRouletteAutoSim import AutoSimulation

SIMULATIONS = 10_000
STARTING_MONEY = 100
GOAL = 200
BET = 10
STRATEGY = "red"


def run_simulations():
    results = [
        AutoSimulation(starting_money=STARTING_MONEY, goal=GOAL, bet=BET, strategy=STRATEGY).run()
        for _ in range(SIMULATIONS)
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
    print("       ROULETTE MONTE CARLO RESULTS")
    print("=" * 45)
    print(f"  Simulations run:     {SIMULATIONS:>10,}")
    print(f"  Starting balance:    ${STARTING_MONEY:>9,}")
    print(f"  Goal balance:        ${GOAL:>9,}")
    print(f"  Bet per round:       ${BET:>9,}")
    print(f"  Strategy:            {STRATEGY:>10}")
    print("-" * 45)
    print(f"  Times goal reached:  {wins:>10,}  ({win_rate:.1f}%)")
    print(f"  Times busted out:    {losses:>10,}  ({100 - win_rate:.1f}%)")
    print("-" * 45)
    print(f"  Avg rounds per game: {avg_rounds:>10.1f}")
    print(f"  Min rounds played:   {min_rounds:>10,}")
    print(f"  Max rounds played:   {max_rounds:>10,}")
    print(f"  Avg final balance:   ${avg_balance:>9.2f}")
    print("=" * 45)


if __name__ == "__main__":
    run_simulations()
