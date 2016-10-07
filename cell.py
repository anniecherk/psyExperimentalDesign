





class Cell(object):
    """

    Attributes:
        instances :: ((name, level))
    """

    def __init__(self, input_tuple):
        """Return an Experiment w. no factors, and no selection-functions"""
        self.instances = input_tuple

    def get_level_by_name(self, name):
        return [elem for elem in self.instances if elem[0]==name][0][1]


    def __iter__(self):
        return iter(self.get_cells())


    def __repr__(self):
         return str(self.instances)
    def __str__(self):
        return str(self.instances)
