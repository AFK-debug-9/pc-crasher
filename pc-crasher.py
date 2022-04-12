input('I (The Creator, ERROR#3317) am not responsible for any damage done or unsaved data lost (I mean which app doesn\'t have auto-save). [Press Enter to Continue]')
import random
a='aaab'
ans = ''
for i in range(10000):
    if random.choice('1234') == '2' or a == '':
        a+=random.choice('ab')
        if random.choice('1234') == '2':
            a+=ans
    ans+=a
    print(f'Iteration: {i+1} out of 10,000 ({(i+1)/100}% complete). Generated: {len(ans)+len(a)} bytes, {(((len(ans)+len(a))/1024)/1024)/1024} GiB')
    b = random.choice(a)
    if b == 'a':
        a=a[1:]
    if b == 'b':
        a=a[1:]
        a+=random.choice('ab')
        
print(f"Your PC... Survived! Congrats! Your PC Genereated {len(ans)+len(a)} bytes! Which is {(((len(ans)+len(a))/1024)/1024)/1024} GiB")
del ans
del a
input('[Press Enter To Exit]')