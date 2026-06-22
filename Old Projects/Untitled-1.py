def power_for(int_base, int_exponent):
    for i in range(int_exponent+1):
        print(int_base*i*i)

def power_while(int_base, int_exponent):
    g = -1
    while g < int_exponent:
        g = g + 1 
        print(int_base*g*g)

def power_recursive(int_base, int_exponent):
    if int_exponent == 0:
        print(1)
    else:
        print(int_base)
        return power_recursive(int_base, int_exponent - 1)


int_base = int(input("base: "))
int_exponent = int(input("exponent: "))

print("for")
power_for(int_base, int_exponent)
print("while")
power_while(int_base, int_exponent)
print("recursive")
power_recursive(int_base, int_exponent)