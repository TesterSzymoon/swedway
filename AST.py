class Instruction:
    def __init__(self):
        pass

class Expr:
    def __init__(self, ins):
        if ins is list:
            self.block = (i for i in ins)
        elif isinstance(ins, Instruction): # not sure if will work
            self.ins = ins

class Function:
    def __init__(self, ident: str, body: Expr):
        self.name = ident
        self.body = body