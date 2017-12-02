class Entity:
    true_list = []
    false_list = []
    next_list = []
    type = None
    place = None
    quad = 0

    @staticmethod
    def backpatch(quad_list, target):
        for quad in quad_list:
            quad.arg_one = target

    def __str__(self):
        return self.place