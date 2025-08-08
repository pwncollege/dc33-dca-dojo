#include <stdio.h>



int main() {

  int rax = 5;
  int rcx = 3;
  int rdx = 4;
  int rdi = 7;
  int rsi = 2;

  unsigned int x = (rax + rcx) * (rdx - rdi) / rsi;
  printf("%d\n", x);
}
