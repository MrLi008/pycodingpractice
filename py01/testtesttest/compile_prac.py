# coding=utf8
import opcode
opmap = opcode.opmap
print opmap

import dis, prac_xor_operator

if __name__  == '__main__':
    filename = 'prac_xor_operator.py'
    source = open(filename).read()

    comp = compile(source, filename, 'exec')

    print type(comp)
    d = dis.dis(comp)
    print d
    dd = dis.dis(prac_xor_operator.decode_xor_operator)
    print dd

