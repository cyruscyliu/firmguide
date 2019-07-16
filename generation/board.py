class Board(object):
    def __init__(self, board_name, soc_name, cpu_type, ncpus=1):
        if ' ' in board_name:
            raise ValueError('Replace the space(s) in board name to the underline(s), like a_b_c.')
        self.board_name = board_name
        self.soc_name = soc_name
        self.cpu_type = cpu_type
        self.ncpus = ncpus

    def get_context(self):
        return self.__dict__
