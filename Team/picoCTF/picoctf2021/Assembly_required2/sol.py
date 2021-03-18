import re
sbuf =  ['copy_char', 'value', '207aLjBod', '1301420SaUSqf', '233ZRpipt', '2224QffgXU', 'check_flag', '408533hsoVYx', 'instance', '278338GVFUrH', 'Correct!', '549933ZVjkwI', 'innerHTML', 'charCodeAt', './aD8SvhyVkb', 'result', '977AzKzwq', 'Incorrect!', 'exports', 'length', 'getElementById', '1jIrMBu', 'input', '615361geljRK','copy_char', 'value', '207aLjBod', '1301420SaUSqf', '233ZRpipt', '2224QffgXU', 'check_flag', '408533hsoVYx', 'instance', '278338GVFUrH', 'Correct!', '549933ZVjkwI', 'innerHTML', 'charCodeAt', './aD8SvhyVkb', 'result', '977AzKzwq', 'Incorrect!', 'exports', 'length', 'getElementById', '1jIrMBu', 'input', '615361geljRK']

def foo(n):
    n=n-0xc3
    n = int(str(n),16)
    print(n)
    return sbuf[n]

def parseInt(n):
    try:
        ret = int(re.search(r'\d+', n).group())
    except:
        ret = 0
    return ret
#print(parsint('sda21235'))

#ans = -parseInt(foo(0xc8)) * -parseInt(foo(0xc9)) + -parseInt(foo(0xcd)) + parseInt(foo(0xcf)) + parseInt(foo(0xc3)) + -parseInt(foo(0xc6)) * parseInt(foo(0xd4)) + parseInt(foo(0xcb)) + -parseInt(foo(0xd9)) * parseInt(foo(0xc7))
#print(ans)
print(foo(0xcc))
