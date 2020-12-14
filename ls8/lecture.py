import sys

#machine that simply executes an instruction

#op-code they represent the instruction that is supposed to be executed

PRINT_HI = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4
PRINT_REGISTER = 5
ADD = 6

memory = [
    PRINT_HI,
    SAVE, 
    65,
    2,
    SAVE,
    20,
    3,
    ADD,
    2,
    3,
    PRINT_REGISTER,
    2,
    HALT,
]

program_counter = 0 # points to current instruction we need to execute next
running = True
registers = [0] *8

#keep looping while not halted

while running:
    command_to_execute = memory[program_counter]

    if command_to_execute == PRINT_HI:
        print("hi")
        program_counter += 1
    elif command_to_execute == PRINT_NUM:
        number_to_print = memory[program_counter + 1]
        print(f"{number_to_print}")
        program_counter += 2
    elif command_to_execute == HALT:
        running = False
        program_counter += 1
    elif command_to_execute == SAVE:
        value_to_save = memory[program_counter +1]
        register_to_save_it_in = memory[program_counter + 2]
        registers[register_to_save_it_in] = value_to_save
        program_counter += 3
    elif command_to_execute == PRINT_REGISTER:
        register_to_print = memory[program_counter +1]
        print(f"{registers[register_to_print]}")
        program_counter += 2
    elif command_to_execute == ADD:
        register_a = memory[program_counter +1]
        register_b = memory[program_counter +2]
        sum_of_registers = registers[register_a] + registers[register_b]
        registers[register_a] = sum_of_registers
        program_counter += 3

    else:
        print(f"Unknown instruction {command_to_execute}")
        sys.exit(1)


