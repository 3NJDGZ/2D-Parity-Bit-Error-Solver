from random import randint

parity_block =[]
temp = []
temp2 = []
temp3 = []
vertical_arrays = []
parity_bits_array= []
num_of_ones = 0

# Check if parity is odd or even
def check(num_of_ones): 
    if num_of_ones % 2 == 0:
        parity_bit = 1
    else:
        parity_bit = 0
    return parity_bit

# Count how many 1s in each sub array
def count_ones(sub_parity_block):
    num_of_ones = 0
    for i in range(7):
        if sub_parity_block[i] == 1:
            num_of_ones += 1
    parity_bit = check(num_of_ones)
    num_of_ones = 0
    return parity_bit

# Creating the Parity bit
def create_parity_bit(parity_block):
    values = []
    for i in range(7):
        sub_parity_block = parity_block[i]
        parity_bit = count_ones(sub_parity_block)
        values.append(parity_bit)
    return values

# Insert Parity Bit into Main List 
def insert_parity_bit(sub_parity_block, parity_bits):
    for i in range(7):
        sub_parity_block.insert(0, parity_bits[i])
    return sub_parity_block

# Tranpose a random bit within the array block
def transpose_random(full_parity_block):
    x = randint(0,7)
    y = randint(0,7)
    if full_parity_block[x][y] == 1:
        full_parity_block[x][y] = 0
    else:
        full_parity_block[x][y] = 1

# Solve Transposed Parity Block
def solve(transposed_parity_block):
    num_of_ones = 0
    row_position = 0
    column_position = 0
    running = True

    # Find Error Row Position 
    for i in range(8):
        for j in range(8):
            if transposed_parity_block[i][j] == 1:
                num_of_ones += 1

        if num_of_ones % 2 == 0:
            row_position = i
            
        num_of_ones = 0
    
    num_of_ones = 0

    # Find Error Column Position
    while running:
        
        for i in range(8):
            for j in range(8):
                if transposed_parity_block[j][i] == 1:
                    num_of_ones += 1
            if num_of_ones % 2 == 0:
                column_position = i
            num_of_ones = 0
        
        running = False

    return[column_position + 1, row_position + 1]

# Instantiate
for i in range(0, 7):
    temp = []

    for j in range(0, 7):
        num = randint(0,1)
        temp.append(num)

    parity_block.append(temp)

# Insert parity bit in front of each subarray within the array
parity_bits = create_parity_bit(parity_block)
for i in range(7):
    parity_block[i].insert(0, parity_bits[i]) 

# Variables to make below iterative processes work
running = True
i = 0
a = 0
count = 0

# Traverse 2 dimensional array from top to bottom 
while running:
    temp3.append(parity_block[i][a])
    i += 1
    if i == 7:
        i = 0
        a += 1
        count += 1
        vertical_arrays.append(temp3)
        temp3 = []
    if count == 8:
        running = False

# Create the other parity bit array for checking vertical values 
running = True
while running:
    for i in range(8):
        for j in range(7):
            if vertical_arrays[i][j] == 1:
                num_of_ones += 1
        if num_of_ones % 2 == 0:
            parity_bits_array.append(1)
        else:
            parity_bits_array.append(0)
        num_of_ones = 0
    running = False

parity_block.append(parity_bits_array)

print("\n-Randomly Generated 8*8 Parity Block-\n")
for i in range(8):
    print(parity_block[i])

print("\n-Transposed One is Below-\n")

transpose_random(parity_block)

for i in range(8):
    print(parity_block[i])
    
print("\n(Counting starts from 1)")
print("\n-Solution-\n")
print("[Column, Row] = " + str(solve(parity_block)))