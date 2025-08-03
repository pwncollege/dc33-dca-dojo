BITS 64
global main
extern printf

section .data
    msg: db "hello, world!", 0
    fmt: db "%c", 10, 0      

section .text
main:

<YOUR CODE GOES HERE>




<YOUR CODE STOPS HERE>   
          

.done:
    mov   eax, 0             
    ret
