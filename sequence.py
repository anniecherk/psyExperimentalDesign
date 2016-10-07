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

# TODO
