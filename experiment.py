from cell import Cell

import itertools
from random import randint


# to do: continuous levels
class Experiment(object):
    """A pyschology experiment. Experiments have factors and rules for selecting sequences:

    Attributes:
        interesting_factors :: List of (name :: string, [levels :: strings])
        confounding_factors :: List of (name :: string, [levels :: strings])
        misc_factors        :: List of (name :: string, [levels :: strings])

        selection_functions :: List of functions with the signature = list of cells -> cell -> bool
             where
          selection_function :: list of trials so far -> trial example -> votes yes or no
    """

    def __init__(self):
        """Return an Experiment w. no factors, and no selection-functions"""
        self.interesting_factors = []
        self.confounding_factors = []
        self.misc_factors = []
        self.selection_functions = []


    def set_interesting_factors(self, factors):
        """Factors are formatted as (name :: string, [levels :: strings])"""
        self.interesting_factors = factors

    def set_confounding_factors(self, factors):
        """Factors are formatted as (name :: string, [levels :: strings])"""
        self.confounding_factors = factors

    def set_misc_factors(self, factors):
        """Factors are formatted as (name :: string, [levels :: strings])"""
        self.misc_factors = factors

    def set_selectors(self, selectors):
        self.selection_functions = selectors

    def cross_important_factors(self): # TODO: Returns a list of cells!
        return list(itertools.product(*(self.interesting_factors + self.confounding_factors)))

    def cross_misc_factors(self):
        return list(itertools.product(*(self.misc_factors)))

    def get_trial_pool(self):
        """ Returns a list of cells! """
        important = self.cross_important_factors()
        misc = self.cross_misc_factors()
        return [Cell(i + misc[randint(0, len(misc)-1)]) for i in important]
