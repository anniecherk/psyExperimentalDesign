#todo: miniblocks
from experiment import Experiment
from factor import Factor
from sequence import Sequence

import random
from copy import deepcopy


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
    return not final.count(final[0].get_level_by_name("task_transition")) == len(final)


task_switching_experiment.set_selectors([repeat_correctly, max_task_repetition])




#print("number of cells of fully crossed factors of interest: " + len(task_switching_experiment.cross_important_factors()))
#print(len(task_switching_experiment.get_trial_pool()))


# ============================================================================================================================================
# =====================   Generate Sequence of Trials  =======================================================================================
# ============================================================================================================================================

trial_pool = task_switching_experiment.get_trial_pool()

for outside_loop in range(0, 3600000):
    cells_to_try = deepcopy(trial_pool)
    resulting_sequence = []
    all_quiet = True #flag to determine whether to give up- might not be most elegant solution

    for i in range(len(trial_pool)): # build up resulting seq
        valid_cells = cells_to_try # init
        for validator in task_switching_experiment.selection_functions:
            # filter remaining trial pool for sequences that can go next
            valid_cells = filter(lambda cell: validator(resulting_sequence, cell), valid_cells)
            if (len(valid_cells) == 0):
                all_quiet = False
                break
        if( not all_quiet ):
            break
        else: #found a good one!
            resulting_sequence.append(random.choice(valid_cells))

    if( all_quiet ): # we made it all the way through! phew!
        break # hooray!
    else:
        if(outside_loop % 1000 == 0):
            print("failed " + str(i))





if(len(resulting_sequence) == 0):
    print("failed!")

else:
    print("succeeded!")
    print(resulting_sequence)










if __name__ == '__main__':
    print("hello world!")
