#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int argv_idx = 0, salutari_idx = 0, i = 0 ;
    int num_salutari = 4;

    char *salutari[num_salutari];

    // a default string
    char *hello = "hello";

    // + 1 is for \0 string terminator

    int hlen = strlen(hello) + 1;

    for (argv_idx = 1, salutari_idx = 0; argv_idx < argc; argv_idx++)
    {
        if (salutari_idx < num_salutari) {
            int len = strlen(argv[argv_idx]) + 1;
            salutari[salutari_idx] = (char *)malloc(sizeof(char) * len);
            memcpy(salutari[salutari_idx], argv[argv_idx], len);
            salutari_idx++;
        }
        printf("arg %d: %s\n", argv_idx, *(argv + argv_idx));
    }

    // If there are not enough arguments to fill all salutari elements put the default string

    printf("salutari_idx = %d\n", salutari_idx);
    for (i = salutari_idx; i < num_salutari; i++) {
        salutari[i] = (char *) malloc(sizeof(char) * hlen);
        memcpy(salutari[i], hello, hlen);
    }

    for (salutari_idx = 0; salutari_idx < num_salutari; salutari_idx++)
    {
        printf("salut %d: %s\n", salutari_idx, *(salutari + salutari_idx));
        free(salutari[salutari_idx]);
    }
    return 0;
}

