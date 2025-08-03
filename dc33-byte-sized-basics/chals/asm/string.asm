BITS 64
global main
extern printf

section .data
    fmt:    db "%s", 10, 0    ; “%s” plus real LF

section .text
main:

<YOUR CODE GOES HERE>




<YOUR CODE STOPS HERE>


mov rax, 60
syscall
