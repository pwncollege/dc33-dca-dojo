#include <stdio.h>

int main(void) {
    const char *msg = "hello, world!";

    for (const char *p = msg; *p != '\0'; ++p) {
       
        printf("%c\n", *p);
    }

    return 0;
}
