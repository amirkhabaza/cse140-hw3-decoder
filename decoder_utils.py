# Instruction Lookup Table based on the RISC-V Green Card
OP_MAP = {
    "0110011": ("R", {"000": {"0000000": "add", "0100000": "sub"}, "001": "sll", "010": "slt", "011": "sltu", "100": "xor", "101": {"0000000": "srl", "0100000": "sra"}, "110": "or", "111": "and"}),
    "0010011": ("I", {"000": "addi", "010": "slti", "011": "sltiu", "100": "xori", "110": "ori", "111": "andi", "001": "slli", "101": {"0000000": "srli", "0100000": "srai"}}),
    "0000011": ("I", {"000": "lb", "001": "lh", "010": "lw"}),
    "1100111": ("I", {"000": "jalr"}),
    "0100011": ("S", {"000": "sb", "001": "sh", "010": "sw"}),
    "1100011": ("SB", {"000": "beq", "001": "bne", "100": "blt", "101": "bge"}),
    "1101111": ("UJ", "jal")
}

def format_imm(val, bit_width):
    """Formats the immediate to match the assignment sample."""
    if val >= 10 or val < 0:
        mask = (1 << bit_width) - 1
        return f"{val} (or 0x{(val & mask):X})"
    return str(val)

def decode_instruction(instr):
    if len(instr) != 32 or not all(c in '01' for c in instr):
        print("Invalid instruction. Please enter a 32-bit binary string.")
        return

    # 1. Extract standard fields
    opcode = instr[25:32]
    rs1 = int(instr[12:17], 2)
    rs2 = int(instr[7:12], 2)
    rd  = int(instr[20:25], 2)
    f3  = instr[17:20]
    f7  = instr[0:7]

    if opcode not in OP_MAP:
        print("Opcode not supported.")
        return

    # 2. Look up instruction type and operation name
    itype, mapping = OP_MAP[opcode]
    op = mapping if itype == "UJ" else mapping.get(f3)
    if isinstance(op, dict): 
        op = op.get(f7)

    # 3. Extract Immediate (Your part needs to fill in S and SB)
    imm_str, bits = "", 0
    
    if itype == "I":
        imm_str, bits = instr[0:12], 12
    elif itype == "UJ":
        imm_str, bits = instr[0] + instr[12:20] + instr[11] + instr[1:11] + "0", 21
    elif itype == "S":
        # TODO: YOUR TASK
        # Slice the 'instr' string to build the S-type immediate.
        # Hint: Look at bits [11:5] and [4:0] on the Green Card.
        imm_str, bits = "000000000000", 12 # Replace this dummy string
    elif itype == "SB":
        # TODO: YOUR TASK
        # Slice the 'instr' string to build the SB-type immediate.
        # Hint: It is shuffled! Look at bits [12], [10:5], [4:1], [11].
        imm_str, bits = "0000000000000", 13 # Replace this dummy string

    # 4. Two's Complement logic for immediate values
    if imm_str:
        imm = int(imm_str, 2)
        if imm_str[0] == '1': 
            imm -= (1 << bits)
        if op in ["slli", "srli", "srai"]: 
            imm &= 0x1F # Shifts only use the lower 5 bits

    # 5. Print results matching the assignment requirements exactly
    print(f"Instruction Type: {itype}")
    print(f"Operation: {op}")
    
    if itype != "UJ": print(f"Rs1: x{rs1}")
    if itype in ["R", "S", "SB"]: print(f"Rs2: x{rs2}")
    if itype in ["R", "I", "UJ"]: print(f"Rd: x{rd}")
    
    if itype == "R":
        print(f"Funct3: {int(f3, 2)}\nFunct7: {int(f7, 2)}")
    else:
        print(f"Immediate: {format_imm(imm, bits)}")