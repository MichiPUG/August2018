from stack_dump import print_traceback, stack_trace
import inspect as ip

def a(arg):
    data1 = "function a"
    data2 = dict(a=1, b='b', c=1.0)
    b(123)

def b(arg):
  data1 = 'function b'
  data2 = [1, 2, 3]
  c(456)

def c(arg):
    data1='function c'
#    print(stack_trace())
    data1[3] = 'a'

try:
    a(0)
except:
    print_traceback()
