from blackJackAutoSim import AutoSimulation

SIMULATIONS = 10_000
STARTING_MONEY = 100
GOAL = 200
BET = 10


def run_simulations():
    # Empty array to hold each game's money 
    run_arr = []

    #commenting out just in case my edited version breaks
    #results = [
    #    AutoSimulation(starting_money=STARTING_MONEY, goal=GOAL, bet=BET).run()
    #    for _ in range(SIMULATIONS)
    #]
    results = []
    for _ in range(SIMULATIONS):
        sim = AutoSimulation(starting_money=STARTING_MONEY, goal=GOAL, bet=BET)
        results.append(sim.run())
        run_arr.append(sim.moneyHistory)

        
    
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


if __name__ == "__main__":
    run_simulations()
