#include <stdio.h>

int main(int argc, char *argv[])
{
	int numbers[4] = {};
	char name[4] = {};

	float f = 3.14;
	int i = *((int*)(float*) &f);
	printf(">> %d %d\n", sizeof(i), i);

	// first, print them raw
	printf("numbers: %d %d %d %d\n",
			numbers[0], numbers[1], numbers[2], numbers[3]);
	printf("name: %d %d %d %d\n",
			name[0], name[1], name[2], name[3]);

	printf("name: %s\n", name);

	// setup the numbers
	numbers[0] = '1';
	numbers[1] = 2;
	numbers[2] = 3;
	numbers[3] = 4;

	// setup the name
	name[0] = 1;
	name[1] = '\0';
	name[2] = '\0';
	name[3] = '\0';

	// print them out initialized
	printf("numbers: %d %d %d %d\n",
			numbers[0], numbers[1], numbers[2], numbers[3]);
	printf("name: %x %x %x %x\n",
			name[0], name[1], name[2], name[3]);

	printf("name: %s\n", name);
	printf(">> %d\n", *(unsigned int*) name);
	

	//another way to use name
	char *another = "Zed";
	printf("another: %s\n", another);
	printf("another: %c %c %c %c\n",
			another[0], another[1], another[2], another[3]);
	return 0;
}
