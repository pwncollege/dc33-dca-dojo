#define _GNU_SOURCE
#include <unistd.h>
#include <sys/syscall.h>
#include <stddef.h>

int main(void) {
    const char msg[] = "Hello from syscalls in main!\n";
    size_t    len   = sizeof(msg) - 1;

   
    syscall(SYS_write,STDOUT_FILENO, 
            msg,len);

    
    syscall(SYS_exit,0);

   
    return 0;
}
