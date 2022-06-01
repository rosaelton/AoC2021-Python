import random
import os

def generate_digits(rows: int, columns: int):
    final_string = ""
    for _ in range(rows):
        for _ in range(columns):
            final_string += str(random.randint(0, 9))
        final_string += "\n"
    final_string = final_string.rstrip("\n")
    return final_string

generated_digits = generate_digits(100, 100)

with open(os.path.join(os.getcwd(),"09.2", "input2"), "w") as f:
    f.write(generated_digits)
