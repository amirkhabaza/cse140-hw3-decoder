# CSE 140 HW3: RISC-V Machine Code Decoder

This repository contains our Python implementation for Homework 3: RISC-V Decoder. The program takes a 32-bit binary machine code string from the user and decodes it into its corresponding RISC-V assembly instruction format.

# Project Structure
main.py: Handles the user interaction, continuously prompting for a 32-bit instruction string until exited.
decoder_utils.py: Contains the actual decoding logic (OP_MAP dictionary and the decode_instruction function).

# What's Already Done (3/4 Complete)
Instruction Mapping: The OP_MAP dictionary is fully set up to map opcodes, funct3, and funct7 to their instruction names (e.g., add, addi, jal, etc.) based on the RISC-V Green Card.
Register Slicing: The standard fields (opcode, rs1, rs2, rd, funct3, funct7) are already being extracted correctly.
Immediate Decoding (R, I, UJ): The immediate value extraction and two's complement sign-extension logic is fully working for I-type and UJ-type instructions.
Formatting: The output strictly matches the format requested in the HW3 PDF (handling cases like 10 (or 0xA)).


Your Task

Your job is to implement the immediate value string slicing for the S-type and SB-type instructions. 

Open decoder_utils.py and look for the PARTNER TASK comments. 

# Task 1: S-Type Immediate
For Store instructions (sb, sh, sw), the immediate is split into two parts on the Green Card:
1. Bits [11:5] (Python index [0:7])
2. Bits [4:0] (Python index [20:25])
Goal:Concatenate these two Python slices to form the 12-bit binary string imm_str.

# Task 2: SB-Type Immediate
For Branch instructions (beq, bne, blt, bge), the bits are scrambled on the Green Card:
1. Bit [12](Python index [0])
2. Bit [11] (Python index [24])
3. Bits [10:5]*(Python index :7)
4. Bits [4:1] (Python index [20:24])
5. Bit [0] is implicitly 0.
Goal: Concatenate these slices and add a 0 at the very end to form the 13-bit binary string imm_str.


# How to Test Your Code
Run the program in your terminal:
```bash
python main.py