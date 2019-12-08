import timeit
def reverse_slicing(s):
    s1=''
    length = len(s)-1
    while length >= 0:
        s1 = s1 +s[length]
        length = length-1
    return s1

def slicing_time():
    SETUP_CODE = '''
from __main__ import reverse_slicing
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_slicing(input_str)
'''
    times = timeit.repeat(setup=SETUP_CODE,
                            stmt=TEST_CODE,
                            repeat=3,
                            number = 10000)
    print(times)
    print('While time : {}'.format(min(times)))
if __name__ == "__main__":
    slicing_time()