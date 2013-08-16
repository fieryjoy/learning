#include <stdio.h>
#include <ctype.h>
#include <string.h>

// forward declarations
void print_letters(char arg[]);

void print_arguments(int argc, char *argv[])
{
	int i = 0;
	for (i = 1; i < argc; i++) {
		print_letters(argv[i]);
	}
}

void print_letters(char arg[])
{
	int i = 0;	
	int len = strlen(arg);
	for(i = 0; i < len; i++) {
		char ch = arg[i];
		if (isdigit(ch) || ispunct(ch)) {
			printf("'%c' == %d ", ch, ch);
		}
	}
	printf("\n");
}

int main(int argc, char *argv[])
{
	print_arguments(argc, argv);
	return 0;
}
