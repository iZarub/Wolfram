import WolframApi

import wolframparser

from Calculation import (real_dependence,
                         Simpson_dependence)


from TestApi import get_integral

import matplotlib.pyplot as plt


if __name__ == "__main__":
    parser = wolframparser.Parser()

    input = "e^(-x)"
    llim = "0"
    rlim = "pi"

    input_for_calculations = parser.convert_to_python_expression(input + "*Cos(k*x)")
    input_for_wolfram = parser.convert_to_wolfram_expression(input)

    simpson_y, ks = Simpson_dependence(input_for_calculations, llim, rlim)
    plt.figure()
    plt.plot(ks, simpson_y, label = "Simpson approximation")

    integral = get_integral(input_for_wolfram, llim, rlim)
    if integral[0]:
        output_python_expr = parser.convert_to_python_expression(integral[1])
        print(output_python_expr)
        real_y, ks = real_dependence(output_python_expr)
        plt.plot(ks, real_y, label = "Real Wolfram Integration")
        plt.grid()
        plt.legend()
        plt.savefig("real.png")
        

    else:
        print(integral[1])

    




