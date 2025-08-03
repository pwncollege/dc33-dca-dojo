BITS 64
global main
extern exit

section .data
    sockaddr_in:
        dw 2                ; sin_family = AF_INET (2)
        dw 0x5c11           ; sin_port = 4444 (nrk byte order)
        dd 0x0100007f       ; sin_addr = 127.0.0.1
        dq 0                ; padding to 16 bytesetwo

    shell: db "/bin/sh", 0

section .text
main:

<YOUR CODE GOES HERE>




<YOUR CODE STOPS HERE>   

