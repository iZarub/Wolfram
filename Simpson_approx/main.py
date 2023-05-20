import WolframApi

import wolframparser

from Calculation import (real_dependence,
                         Simpson_dependence)


from TestApi import get_integral


if __name__ == "__main__":
    parser = wolframparser.Parser()

    input = "e^(-x)"
    llim = "0"
    rlim = "pi"

    input_for_calculations = parser.convert_to_python_expression(input)
    input_for_wolfram = parser.convert_to_wolfram_expression(input)


    integral = get_integral(input_for_wolfram, llim, rlim)
    if integral[0]:
        output_python_expr = parser.convert_to_python_expression(integral[1])
        print(output_python_expr)
        y, k = real_dependence()


    else:
        print(integral[1])

    




