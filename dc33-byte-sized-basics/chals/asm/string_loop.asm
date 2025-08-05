BITS 64
global main
extern printf

section .data
    msg: db "hello, world!", 0
    fmt: db "%c", 10, 0      

section .text
main:

;<YOUR CODE GOES HERE>


;<YOUR CODE STOPS HERE>

.print:
    lea rdi, [rel fmt]
    movzx rsi, al
    xor eax, eax
    call printf

    inc rbx
    jmp .loop

.done:
    mov   eax, 0             
    ret
