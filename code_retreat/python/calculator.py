
class CalculationException(Exception):
    pass

class Calculator:



    def _validate_input(self, input):
        if not isinstance(input, str):
            raise Exception()

    def _parse_number_string(self, number):
        if len(number) == 0:
            return False, None
        try:
            parsed_number = int(number)
            return True, parsed_number
        except:
            raise CalculationException()


    def calculate(self, input):
        self._validate_input(input)

        numbers = input.split(',')
        result = 0

        for number in numbers:
            parsed_number = self._parse_number_string(number)
            if parsed_number[0] == False:
                continue
            result = int(number) + result
        return result