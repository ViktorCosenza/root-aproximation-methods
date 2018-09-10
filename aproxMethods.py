def derivative(x):
    return 3 * (x**2) - 9

def f(x):
    return x**3 - 9*x + 3

def tangentMethod(initial_x = 1, tolerance = 0.01, MAX_ITERATIONS = 20):
    x = initial_x
    iteration = 0
    while (iteration < MAX_ITERATIONS):
        x = x - (f(x) / derivative(x))
        if abs(f(x)) < tolerance:
            print('Iteration: ' + str(iteration))
            print('x: ' + str(x))
            print('f(x): ' + str(f(x)))
            return x
        iteration += 1
    print('ERR: MAX NUMBER OF ITERATIONS')

def secantMethod(x0, x1, rootTolerance = 0.01, differenceTolerance = 0.001, MAX_ITERATIONS = 20):
    iteration = 0
    while (iteration < MAX_ITERATIONS):
        x2 = x1 - (f(x1) * ((x1 - x0) / (f(x1) - f(x0))))
        if(abs(f(x2)) < rootTolerance or abs(x2 - x1) < differenceTolerance):
            print('Iteration: ' + str(iteration))
            print('x: ' + str(x2))
            print('f(x): ' + str(f(x2)))
            return x2
        x0 = x1
        x1 = x2
        iteration += 1
    print('ERR: MAX NUMBER OF ITERATIONS')
     
def main():
    print("\nF(x) = x^3 - 9x + 3")
    print('\n    METODO DA TANGENTE')
    tangentMethod(0.75, 0.01, 20)
    print('\n    METODO DA SECANTE')
    secantMethod(0, 0.75)

if __name__ == "__main__":
    main()
