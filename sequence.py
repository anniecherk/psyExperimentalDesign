import itertools

# to do: continuous levels
class Sequence(object):
    """A sequence represents the sequence of cells we've already selected.
    It has support to optionally contain mini-blocks, blocks, and sessions.
    We reset the sequence when we fail to construct a valid sequence.

    Attributes:
        trials :: List of Tuples of Cells
    """

    def __init__(self):
        "Return a sequence with no mini-blocks, blocks or sessions"
        self.trials = []
        self.trials_per_miniblock = sys.maxint
        self.trials_per_block = sys.maxint
        self.trials_per_session = sys.maxint

    def add_trial(self, factor):
        self.trials.append(factor)

#     def get_current_sequence
#
#
#     def set_interesting_factors(self, factors):
#         """Factors are formatted as (name :: string, [levels :: strings])"""
#         self.interesting_factors = factors
#
#     def set_confounding_factors(self, factors):
#         """Factors are formatted as (name :: string, [levels :: strings])"""
#         self.confounding_factors = factors
#
#     def set_misc_factors(self, factors):
#         """Factors are formatted as (name :: string, [levels :: strings])"""
#         self.misc_factors = factors
#
#     def set_selectors(self, selectors):
#         self.selection_functions = selectors
#
#     def cross_important_factors(self):
#         return list(itertools.product(*(self.interesting_factors + self.confounding_factors)))
#
# # to do: def glom_misc_factors(self):
# # to do: create trial set
