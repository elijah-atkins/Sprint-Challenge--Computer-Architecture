# a = 0b1001
# b = a << 2 #0b100100
# c = a >> 2 #0b10

# print (bin(b),bin(c),c)

INSTRUCTIONS = 0b1000010 # >>6 --> 0b10
PC = 0
number_of_times_to_increment_pc = ((INSTRUCTIONS >> 6) & 0b11) +1
print (number_of_times_to_increment_pc)