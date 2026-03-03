from decoder_utils import decode_instruction

def main():
    while True:
        try:
            instruction = input("Enter an instruction:\n").strip()
            if not instruction:
                break
            
            # Call the processing function from our utils file
            decode_instruction(instruction)
            
        except EOFError:
            break

if __name__ == "__main__":
    main()