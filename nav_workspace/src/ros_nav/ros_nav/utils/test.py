from motor_serial import int_to_str_bits

result = int_to_str_bits(-1, 8)
if result != '11111111':
    print("RESULT NOT CORRECT:" + result)

result = int_to_str_bits(-128, 8)
if result != '10000000':
    print("RESULT NOT CORRECT:" + result)

result = int_to_str_bits(-128, 8)
if result != '10000000':
    print("RESULT NOT CORRECT:" + result)

result = int_to_str_bits(-30, 6)
if result != '100010':
    print("RESULT NOT CORRECT:" + result)

result = int_to_str_bits(30, 6)
if result != '011110':
    print("RESULT NOT CORRECT:" + result)

print("Tests done")