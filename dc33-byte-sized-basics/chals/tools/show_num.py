
num_str = input("Enter a number (decimal or 0x-hex): ").strip()


n = int(num_str, 0)


mask64 = (1 << 64) - 1
bits64 = n & mask64


print(f"{bits64:064b}")
