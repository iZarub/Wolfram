OUTPUT_SYMBOLS = {
    "^" : "**",
    "[" : "(",
    "]" : ")",
    "Cos": "math.cos",
    "Sin": "math.sin",
    "Pi" : "math.pi",
    "Log": "math.log",
    "e": "math.exp(1)",
    # "cos": "math.cos",
    # "sin" : "math.sin"
}


INPUT_SYMBOLS = {
    "inf" : "Infinity",
    "infty": "Infinity",
    "pi" : "Pi",
    "sin": "Sin",
    "cos": "Cos",
    "ln": "Ln",
    "log" : "Ln",
    "sqrt": "Sqrt",
    

}


class Parser():
    '''
    Класс необходимый для парсинга вводимых вручную формул, поскольку
    в запрос в юрл нельзя вводить символы типа "^".????
    Предполагается, что ввод будет в классическом wolfram alpha стиле.

    В вольфраме строки парсятся классической командой 'ToExpression["String"]'.

    Также необходим для парсинга полученного в json респонсе ответа от
    Вольфрама. Строки переводятся в нормальный вид и преобразуются
    классическим образом eval()
    '''
    def __init__(self):
        self.output_symbols = OUTPUT_SYMBOLS
        self.input_symbols = INPUT_SYMBOLS


    def convert_to_python_expression(self, output: str) -> str:
        for elem in self.output_symbols:
            output = output.replace(elem, self.output_symbols[elem])
        return output


    def convert_to_wolfram_expression(self, input: str) -> str:
        for elem in self.input_symbols:
            input = input.replace(elem, self.input_symbols[elem])
        return input