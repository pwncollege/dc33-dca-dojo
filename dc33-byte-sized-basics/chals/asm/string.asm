BITS 64
global main
extern printf

section .data
    fmt:    db "%s", 10, 0
    fmt1:   db  "rsp = %llx", 10, 0

section .text

print_rsp:
  sub rsp, 8
  mov rdi,fmt1
  mov rsi, rsp
  xor rax,rax
  call printf
  add rsp,8
  ret

main:

;<YOUR CODE GOES HERE>


;<YOUR CODE STOPS HERE>


lea rdi, [rel fmt]
mov rsi, rsp
xor eax, eax
call printf
add rsp, 8

mov rax, 60
syscall
