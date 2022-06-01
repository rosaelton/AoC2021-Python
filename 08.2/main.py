import os

from sklearn.metrics import zero_one_loss

def handle_lines(lines: list[str]) -> list:
    input_lines = []
    for line in lines:
        line = line.rstrip("\n")
        line = line.split(" ")
        input_lines.append(line)
    
    return input_lines


def decoded_display_sum(basic_inputs: list[str]) -> tuple[int]:
    decoded_sum = 0
    for line in basic_inputs:

        pattern = line[:-5]
        encoded_display = line[-4:]

        results = {
        "zero": [],
        "one": [],
        "two": [],
        "three": [],
        "four": [],
        "five": [],
        "six": [],
        "seven": [],
        "eight": [],
        "nine": []
        }

        for num in pattern:
            match len(num):
                case 2:
                    results["one"].append(num)
                case 3:
                    results["seven"].append(num)
                case 4:
                    results["four"].append(num)
                case 5:
                    results["two"].append(num)
                    results["three"].append(num)
                    results["five"].append(num)
                case 6:
                    results["zero"].append(num)
                    results["six"].append(num)
                    results["nine"].append(num)
                case 7:
                    results["eight"].append(num)
        
        # Wire 1
        for letter in results['seven'][0]:
            if letter not in results['one'][0]:
                wire_1 = letter
                break

        # Wire 3
        for letter in results['one'][0]:
            for word in results['zero']:
                if letter not in word:
                    wire_3 = letter
                    break
        
        # Wire 6
        for letter in results['one'][0]:
            if letter != wire_3:
                wire_6 = letter
                break
        
        # Wire 7
        words: list[str] = results['nine'].copy()
        for index, word in enumerate(results['nine']):
            if wire_1 in word:
                words[index] = words[index].replace(wire_1, "")
            if wire_3 in word:
                words[index] = words[index].replace(wire_3, "")
            if wire_6 in word:
                words[index] = words[index].replace(wire_6, "")
        
        ref_word = ""
        appearing_thrice = []
        for word in words:
            if len(word) == 4:
                ref_word = word
                break

        for letter in ref_word:
            if letter in words[0] and letter in words[1] and letter in words[2]:
                appearing_thrice.append(letter)
        
        for letter in appearing_thrice:
            if letter not in results['four'][0]:
                wire_7 = letter
                break
        
        # wire 2
        for letter in appearing_thrice:
            if letter != wire_7:
                wire_2 = letter
        
        # Wire 1, Wire 2, Wire 3, Wire 6, Wire 7
        # Missing: Wire 4, Wire 5
        
        # Wire 4
        words: list[str] = results['two'].copy()
        appearing_thrice = []
        for letter in words[0]:
            if letter in words[0] and letter in words[1] and letter in words[2]:
                appearing_thrice.append(letter)
        
        appearing_thrice.remove(wire_1)
        appearing_thrice.remove(wire_7)
        wire_4 = appearing_thrice[0]

        # Wire 5
        eight = results['eight'][0]
        eight = eight.replace(wire_1, "")
        eight = eight.replace(wire_2, "")
        eight = eight.replace(wire_3, "")
        eight = eight.replace(wire_4, "")
        eight = eight.replace(wire_6, "")
        eight = eight.replace(wire_7, "")
        wire_5 = eight

        # Wire Patterns
        zero_wire_pattern = (1, 2, 3, 5, 6, 7)
        one_wire_pattern = (3, 6)
        two_wire_pattern = (1, 3, 4, 5, 7)
        three_wire_pattern = (1, 3, 4, 6, 7)
        four_wire_pattern = (2, 3, 4, 6)
        five_wire_pattern = (1, 2, 4, 6, 7)
        six_wire_pattern = (1, 2, 4, 5, 6, 7)
        seven_wire_pattern = (1, 3, 6)
        eight_wire_pattern = (1, 2, 3, 4, 5, 6, 7)
        nine_wire_pattern = (1, 2, 3, 4, 6, 7)

        wires = (wire_1, wire_2, wire_3, wire_4, wire_5, wire_6, wire_7)
        
        decoded_number = ""
        for encoded_number in encoded_display:
            indexes = []
            for letter in encoded_number:
                indexes.append(wires.index(letter) + 1)
            indexes = sorted(indexes)
            indexes = tuple(indexes)

            digits = ""

            if indexes == zero_wire_pattern:
                digits += "0"
            elif indexes == one_wire_pattern:
                digits += "1"
            elif indexes == two_wire_pattern:
                digits += "2"
            elif indexes == three_wire_pattern:
                digits += "3"
            elif indexes == four_wire_pattern:
                digits += "4"
            elif indexes == five_wire_pattern:
                digits += "5"
            elif indexes == six_wire_pattern:
                digits += "6"
            elif indexes == seven_wire_pattern:
                digits += "7"
            elif indexes == eight_wire_pattern:
                digits += "8"
            elif indexes == nine_wire_pattern:
                digits += "9"

            decoded_number += digits
        
        decoded_number = int(decoded_number)
        decoded_sum += decoded_number


    return decoded_sum

if __name__ == "__main__":

    cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(cwd, "input"), "r") as f:
        lines = f.readlines()

    patterns = handle_lines(lines)

    summation = decoded_display_sum(patterns)
    print(summation)
    