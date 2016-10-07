





class Factor(object):
    """

    Attributes:
        name :: string,
        levels :: [strings] ---- might need to be numeric!!
    """

    def __init__(self, input_name, input_levels):
        """Return an Experiment w. no factors, and no selection-functions"""
        self.name = input_name
        self.levels = input_levels

    def get_cells(self):
        """represent as [(name, level)] easier for sequencing..."""
        return [(self.name, level) for level in self.levels]

   # to do
    def __iter__(self):
        return iter(self.get_cells())
