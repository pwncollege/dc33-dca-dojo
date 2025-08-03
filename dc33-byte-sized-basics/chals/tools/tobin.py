#!/usr/bin/python3
import sys, subprocess

USAGE = 'Usage: ./tobin.py { -b | -h | -j } "instr1; instr2; …"'

def asm_hex(instr):
    p = subprocess.run(["rasm2","-a","x86","-b","64",instr], capture_output=True, text=True)
    if p.returncode != 0 or not p.stdout.strip():
        sys.stderr.write(f"asm error for: {instr}\n{p.stderr}\n")
        sys.exit(1)
    return p.stdout.strip()

def spaced(h):
    return " ".join(h[i:i+2] for i in range(0, len(h), 2))

def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("-b","-h","-j"):
        print(USAGE)
        sys.exit(1)
    mode, line = sys.argv[1], sys.argv[2]
    instrs = [s.strip() for s in line.split(";") if s.strip()]
    for ins in instrs:
        h = asm_hex(ins)
        b = bytes.fromhex(h)
        if mode == "-b":
            print(ins)
            for byte in b:
                print(f"{byte:08b}")
            print()
        elif mode == "-h":
            print(ins)
            print(spaced(h))
            print()
        else:
            print(f"{spaced(h)}\t{ins}\t{len(b)}")

if __name__ == "__main__":
    main()
