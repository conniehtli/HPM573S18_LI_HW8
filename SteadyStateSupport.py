import scr.FormatFunctions as Format
import scr.FigureSupport as Fig
import scr.StatisticalClasses as Stat
import Parameters as P

def print_outcomes(sim_output, coin_type):

    reward_mean_CI_text = Format.format_estimate_interval(
        estimate=sim_output.get_ave_reward(),
        interval=sim_output.get_CI_reward(alpha=P.ALPHA),
        deci=1)

    print(coin_type)
    print("Estimate of game reward and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          reward_mean_CI_text)


def draw_reward_histograms(sim_output_fair_coin, sim_output_unfair_coin):

    set_of_game_rewards = [
        sim_output_fair_coin.get_rewards(),
        sim_output_unfair_coin.get_rewards()
    ]

    Fig.graph_histograms(
        data_sets=set_of_game_rewards,
        title='Histogram of game reward',
        x_label='Game rewards',
        y_label='Counts',
        bin_width=50,
        legend=['Fair Coin', 'Unfair Coin'],
        transparency=0.6
    )

def print_comparative_outcomes(sim_output_fair_coin, sim_output_unfair_coin):

    difference = Stat.DifferenceStatIndp(
        name='Change in game rewards',
        x=sim_output_unfair_coin.get_rewards(),
        y_ref=sim_output_fair_coin.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=difference.get_mean(),
        interval=difference.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Average change in game rewards and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)