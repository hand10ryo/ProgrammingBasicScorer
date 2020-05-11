def function1():
    print("function1: run")

def function2():
    print("function2: start")
    function1()
    print("function2: end")

print("main routine: start")
function1()
function2()
print("main routine: end")
