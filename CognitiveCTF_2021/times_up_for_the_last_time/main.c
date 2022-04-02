/*
CognitiveCTFのShell上の操作
cd ~
gcc main.c -o main
cd purpose dir
~/main
*/

#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
/* reference */
/* https://github.com/AMACB/picoCTF-2019-writeups/blob/master/problems/times-up-for-the-last-time/README.md */

int main() {
    signal(SIGALRM, SIG_IGN);
    system("./times-up-one-last-time");
}