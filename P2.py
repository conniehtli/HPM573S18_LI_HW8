import Parameters as P
import Classes as Cls
import TransientStateSupport as Support

# create multiple game sets for when the coin is fair
FairCoinMultiGame = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_SETS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    prob_head=[P.FAIR_PROB_HEAD] * P.NUM_SIM_SETS,  # [p, p, ...]
    n_games_in_a_set=[P.REAL_SET_SIZE] * P.NUM_SIM_SETS  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
)
# simulate all game sets
FairCoinMultiGame.simulation()

# create multiple game sets for when the coin is unfair
UnfairCoinMultiGame = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_SETS, 2*P.NUM_SIM_SETS),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    prob_head=[P.UNFAIR_PROB_HEAD] * P.NUM_SIM_SETS,
    n_games_in_a_set=[P.REAL_SET_SIZE] * P.NUM_SIM_SETS  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
)

# simulate all game sets
UnfairCoinMultiGame.simulation()

# print outcomes of each cohort
Support.print_outcomes(FairCoinMultiGame, 'When the probability of flipping a head is 0.5:')
Support.print_outcomes(UnfairCoinMultiGame, 'When the probability of flipping a head is 0.45')

# draw histograms of average survival time
Support.draw_histograms(FairCoinMultiGame, UnfairCoinMultiGame)

# print comparative outcomes
Support.print_comparative_outcomes(FairCoinMultiGame, UnfairCoinMultiGame)