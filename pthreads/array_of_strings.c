#include <stdio.h>
#include <string.h>

int main() 
{
	char *names[10] = {};
	int i;
	for (i = 0; i < 10; i++) 
	{
		names[i] = "Same";
		strcat(names[i], " Hello");
	}
}
