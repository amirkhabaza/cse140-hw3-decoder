# CSE 140 HW3: RISC-V Machine Code Decoder

Team Members: Amir Khabaza & Lassi Sevanto

It takes a 32-bit binary machine code string and decodes it into its corresponding RISC-V assembly instruction format, identifying the instruction type, operation name, registers, and immediate values.

# Division of Labor
As required by the assignment guidelines, our team divided the decoding implementations:

 Amir Khabaza: Designed the core architecture and the OP_MAP dictionary mapping.
   Implemented the standard field extraction (opcode, rs1, rs2, rd, funct3, funct7).
   Implemented the immediate extraction and two's complement logic for R-type, I-type, and UJ-type instructions.
   Handled the hex-formatting requirements for the final console output.
 Lassi Sevanto:
   Implemented the complex bit-slicing and immediate string reconstruction for the  S-type (Store) instructions.
   Implemented the scrambled bit-slicing and immediate string reconstruction for the SB-type (Branch) instructions.

# How It Works (The Logic)
1. Opcode Parsing: The rightmost 7 bits [25:32] are parsed to determine the instruction type (R, I, S, SB, UJ).
2. Dictionary Lookup: The opcode, funct3, and funct7 are passed into our OP_MAP to retrieve the exact operation (e.g., addi, jal, sb).
3. Register Slicing: Fixed Python indices extract the binary values for registers, which are converted to integers (e.g., x4, x12).
4. Immediate Reconstruction: Based on the instruction type, the immediate bits are sliced, reordered (for S, SB, and UJ types), padded with implicit zeros, and passed through a Two's Complement check for negative values.
5. Masking: Shift instructions (slli, srli, srai) have their immediates masked to 5 bits (& 0x1F) per RISC-V specifications.

# How to Run the Demo
Run the program in the terminal:
python main.py


Test Results
1. Enter an instruction:
00000000001100100000001010110011
Instruction Type: R
Operation: add
Rs1: x4
Rs2: x3
Rd: x5
Funct3: 0
Funct7: 0

2. Enter an instruction:
00000000101001100111011010010011         
Instruction Type: I
Operation: andi
Rs1: x12
Rd: x13
Immediate: 10 (or 0xA)

3. Enter an instruction:
11111110001100100000100000100011
Instruction Type: S
Operation: sb
Rs1: x4
Rs2: x3
Immediate: -16 (or 0xFF0)

4. Enter an instruction:
00000001111000101001001101100011
Instruction Type: SB
Operation: bne
Rs1: x5
Rs2: x30
Immediate: 6