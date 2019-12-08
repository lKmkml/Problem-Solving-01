import timeit
def reverse_recursion(s):
    if len(s)==0:
        return s
    else :
        return reverse_recursion(s[1:])+s[0]

def recursion_time():
    SETUP_CODE = '''
from __main__ import reverse_recursion
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_recursion(input_str)
'''
    times = timeit.repeat(setup=SETUP_CODE,
                            stmt=TEST_CODE,
                            repeat=3,
                            number = 10000)
    print(times)
    print('recursive time : {}'.format(min(times)))
if __name__ == "__main__":
    recursion_time()