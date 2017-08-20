# coding=utf8


if __name__  == '__main__':
    filename = 'prac_xor_operator.py'
    source = open(filename).read()

    comp = compile(source, filename, 'exec')

    print type(comp)

