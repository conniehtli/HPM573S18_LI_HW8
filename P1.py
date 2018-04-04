import Parameters as P
import Classes as Cls
import SteadyStateSupport as Support


FairCoinGames = Cls.SetOfGames(id=1, prob_head=P.FAIR_PROB_HEAD, n_games=P.SIM_SET_SIZE)

FairCoinOutcome = FairCoinGames.simulation()


UnfairCoinGames = Cls.SetOfGames(id=2, prob_head=P.UNFAIR_PROB_HEAD, n_games=P.SIM_SET_SIZE)

UnfairCoinOutcome = UnfairCoinGames.simulation()

# print outcomes of each cohort
Support.print_outcomes(FairCoinOutcome, 'When the probability of flipping a head is 0.5:')
Support.print_outcomes(UnfairCoinOutcome, 'When the probability of flipping a head is 0.45:')

# draw survival curves and histograms
Support.draw_reward_histograms(FairCoinOutcome, UnfairCoinOutcome)

# print comparative outcomes
Support.print_comparative_outcomes(FairCoinOutcome, UnfairCoinOutcome)
