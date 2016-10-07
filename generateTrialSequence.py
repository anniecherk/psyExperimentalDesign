#todo: miniblocks
from experiment import Experiment
from factor import Factor
from sequence import Sequence

import random


# ============================================================================================================================================
# ============================   Set up the Experiment =======================================================================================
# ============================================================================================================================================
task_switching_experiment = Experiment()

#~~~~ Factors of Interest ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
feature_correlation           = Factor("feature_correlation", ["uncorrelated", "correlated"])
congruency                    = Factor("congruency", ["incongruent", "congruent"])
task_transition               = Factor("task_transition", ["repeat", "switch"])
irrelevant_feature_transition = Factor("irrelevant_feature_transition", ["low", "high"])

task_switching_experiment.set_interesting_factors([feature_correlation, congruency, task_transition, irrelevant_feature_transition])

#~~~~ Confounding Factors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
task                = Factor("task", ["color task", "motion task"])
response            = Factor("response", ["left", "right"])
response_transition = Factor("response_transition", ["repeat", "switch"])

task_switching_experiment.set_confounding_factors([task, response, response_transition])

#~~~~ Misc Factors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
color          = Factor("color", ["blue", "red"])
motion         = Factor("motion", ["up", "down"])
miniblock_size = Factor("miniblock_size", [4, 5, 6])

task_switching_experiment.set_misc_factors([color, motion, miniblock_size])

#~~~~ Selection Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#def transition_selector(seq_so_far, trial_to_consider):
#    return

def repeat_correctly(seq_so_far, trial_to_consider):
    if(len(seq_so_far) == 0):
        return True

    last_elem = seq_so_far[-1] #a cell

    if (last_elem.get_level_by_name("task_transition") == "repeat"):
        correct_task_transition = trial_to_consider.get_level_by_name("task") == last_elem.get_level_by_name("task") # make sure they're the same task
    else:
        correct_task_transition = trial_to_consider.get_level_by_name("task") != last_elem.get_level_by_name("task") # make sure they're different tasks
    if(last_elem.get_level_by_name("response_transition") == "repeat"):
        correct_response_transistion = trial_to_consider.get_level_by_name("response") == last_elem.get_level_by_name("response")
    else:
        correct_response_transistion = trial_to_consider.get_level_by_name("response") != last_elem.get_level_by_name("response")

    return correct_task_transition and correct_response_transistion # compute boolean and as validator


def max_task_repetition(seq_so_far, trial_to_consider):
    n = 7

    if(len(seq_so_far) < n):
        return True

    final = seq_so_far[-(n-1):] + seq_so_far
    return final.count(final[0].get_level_by_name("task_transition")) == len(final)


task_switching_experiment.set_selectors([repeat_correctly, max_task_repetition])

# def yes(seq_so_far, trial_to_consider):
#     return True
#
# task_switching_experiment.set_selectors([yes])






#print("number of cells of fully crossed factors of interest: " + len(task_switching_experiment.cross_important_factors()))
print(len(task_switching_experiment.get_trial_pool()))



# ============================================================================================================================================
# =====================   Generate Sequence of Trials  =======================================================================================
# ============================================================================================================================================
''' Trial Sequence Generation:
- cross all interesting & confounding factors
- pseudo-randomly sample misc factors and concat them on
- try (10,00 times) to generate a valid ordering, by generating and then validiating
    - print failure number
- output list of crossings '''

trial_pool = task_switching_experiment.get_trial_pool()
resulting_sequence = []

for i in range(0, 3628800):
    ordering = random.sample(trial_pool, len(trial_pool))   # guess an ordering for the sequence
    all_quiet = True #flag to determine whether to give up- might not be most elegant solution

    for x in ordering:
        for validator in task_switching_experiment.selection_functions:
            if (not validator(resulting_sequence, x)):
                all_quiet = False
                resulting_sequence = []
                if(i % 1000 == 0):
                    print("failed " + str(i))
                break
        if( all_quiet ):
            resulting_sequence.append(x)
        else:
            break

    if( all_quiet and (len(resulting_sequence) == len(trial_pool)) ): #sanity check
        break #hooray!


if(len(resulting_sequence) == 0):
    print("failed!")
else:
    print("succeeded!")







def get_sequence(trial_pool, ordering):
    [trial_pool[i] for i in ordering]



# for (i < 10,000)
#    current_trial_pool = trial_pool #todo! Deep copy!
#    result_sequence = []
#    while (current_trial_pool not empty)
#       candidate = randomly select from trial pool
#       if all( map (func, candidate) func(candidate) all_selector_functions ):
#           result_sequence.append(candidate)
#       else:
#           current_trial_pool = [] # hacky and also wrong!
#




if __name__ == '__main__':
    print("hello world!")
