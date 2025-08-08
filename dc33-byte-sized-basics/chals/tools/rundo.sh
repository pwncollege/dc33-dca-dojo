#!/usr/bin/bash
shopt -s extglob

f=$1

f1=${f::-4}

nasm -f elf64 "$f1".asm -o "$f1".o

gcc -no-pie "$f1".o -o "$f1"

./"$f1"

echo "Exit code: $?"

rm -rf asm/*.o
for f in asm/*; do
  if [[ -f $f && $f != *.* ]]; then
    rm -- "$f"
  fi
done

