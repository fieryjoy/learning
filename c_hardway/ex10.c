#include <stdio.h>
#include <stdlib.h>

// python -c  'import os; os.system("./ex10.o " + " ".join([str(el) for el in range(1, 23695)]))'

int main(int argc, char * argv[])
{
	int i = 0;

	if (argc == 1) {
		printf("You have no arguments. You suck.\n");
		exit(EXIT_FAILURE);
	} else if(argc > 1 && argc < 4) {
		printf("Here's your arguments:\n");
		for (i = 1; i < argc; i++) {
			printf("%s ", argv[i]);
		}
		printf("\n");
	} else {
		printf("You have too many arguments. You suck.\n");
		exit(EXIT_FAILURE);
	}	
	
	// let's make our own array of strings
	char *states[] = {
		"California", "Oregon",
		"Washington", "Texas"
	};

	int num_states = 4;

	for (i = 0; i < num_states; i++) {
		printf("state %d: %s\n", i, states[i]);
	}

	return 0;
}
