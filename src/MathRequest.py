class MathRequest:

    def __init__ (self, ope1, ope, ope2):
        self.ope1 = ope1
        self.ope = ope
        self.ope2 = ope2
        self.result = None

    def get_ope1(self):
        return self.ope1

    def get_ope(self):
        return self.ope

    def get_ope2(self):
        return self.ope2

    def get_res(self):
        return self.result

    def set_res(self, value):
        self.result =  value

    def to_string(self):
        raise NotImplementedError