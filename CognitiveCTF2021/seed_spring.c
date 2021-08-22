#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int i, num;
    unsigned int seed;
    unsigned int shift;
    unsigned int ans;
    
    seed = time(NULL);
    srand(seed);

    for (i = 0; i < 50; i++) {
        num = rand();
	shift = (uint)(num >> 0x1f) >> 0x1b;
	ans = (num + shift & 0x1f) - shift;
	printf("%2d\n", ans);
    }
    return 0;
}
