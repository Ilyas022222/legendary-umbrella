from modules.input_module import get_input
from modules.process_module import add, subtract, multiply, divide
from modules.output_module import display_result # type: ignore

num1, num2 = get_input()

sum_result = add(num1, num2)
differece_result = subtract(num1, num2)
product_result = multiply(num1, num2)
Quotient_result = divide(num1, num2)

display_result(sum_result, "sum", num1, num2)
display_result(differece_result, "difference", num1, num2)
display_result(product_result, "product", num1, num2)
display_result(Quotient_result, "quotient", num1, num2)

