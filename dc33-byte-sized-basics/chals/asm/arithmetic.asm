BITS 64
GLOBAL main 


extern printf

section .data
    fmt     db  "RAX = %llx", 10, 0

section .text

print_rax:
  sub rsp, 8 
  mov rdi,fmt
  mov rsi, rax 
  xor rax,rax 
  call printf
  add rsp,8 
  ret


main:
<YOUR CODE GOES HERE>




<YOUR CODE STOPS HERE>

call print_rax

mov rax,60
syscall
