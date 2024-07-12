a = 5
def func():
    global a
    a += 1
    print(a)

print()
func()