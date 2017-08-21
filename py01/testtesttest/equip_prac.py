# coding=utf8
from equip import Instrumentation, MethodVisitor, SimpleRewriter


def simpleshow(s):
    if isinstance(s, str):
        print 'in simple show: ', s
    else:
        print 'in simple show: ', str(s)



class MethodInstr(MethodVisitor):

    def __init__(self):
        MethodVisitor.__init__(self)


    def visit(self, methodDecl):
        rewriter = SimpleRewriter(methodDecl)

        rewriter.insert_before(simpleshow)



if __name__ == '__main__':


    instr_vistor = MethodInstr()
    instr = Instrumentation('..')
    if instr.prepare_program():
        instr.apply(instr_vistor, rewrite=True)