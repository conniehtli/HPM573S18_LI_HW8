import scr.FormatFunctions as Format
import scr.FigureSupport as Fig
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(multi_gameset, coin_type):

    reward_mean_PI_text = Format.format_estimate_interval(
        estimate=multi_gameset.get_overall_mean_reward(),
        interval=multi_gameset.get_PI_mean_reward(alpha=P.ALPHA),
        deci=1)

    print(coin_type)
    print("  Estimate of mean game reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          reward_mean_PI_text)


def draw_histograms(multi_cohort_fair_coin, multi_cohort_unfair_coin):

    set_of_game_rewards = [
        multi_cohort_fair_coin.get_all_mean_reward(),
        multi_cohort_unfair_coin.get_all_mean_reward()
    ]

    # graph histograms
    Fig.graph_histograms(
        data_sets=set_of_game_rewards,
        title='Histogram of average game reward',
        x_label='Game reward',
        y_label='Counts',
        bin_width=50,
        legend=['Fair Coin', 'Unfair Coin'],
        transparency=0.5,
    #    x_range=[-50, 0]
    )


def print_comparative_outcomes(multi_cohort_fair_coin, multi_cohort_unfair_coin):

    difference = Stat.DifferenceStatIndp(
        name='Change in expected reward',
        x=multi_cohort_unfair_coin.get_all_mean_reward(),
        y_ref=multi_cohort_fair_coin.get_all_mean_reward()
    )

    estimate_CI = Format.format_estimate_interval(
        estimate=difference.get_mean(),
        interval=difference.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Expected change in mean game reward and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          estimate_CI)
