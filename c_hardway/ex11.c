#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int argv_idx = 0, states_idx = 0, i = 0 ;
	int num_states = 4;

	char *states[num_states];
	char *hello = "";
	int hlen = strlen(hello) + 1;

	for (argv_idx = 1, states_idx = 0; argv_idx < argc; argv_idx++)
	{
		if (states_idx < num_states) {
			int len = strlen(argv[argv_idx]) + 1;
			states[states_idx] = (char *)malloc(sizeof(char) * len);
			memcpy(states[states_idx], argv[argv_idx], len);
			states_idx++;
		}
		printf("arg %d: %s\n", argv_idx, argv[argv_idx]);
	}

	printf("states_idx = %d\n", states_idx);	
	for (i = states_idx; i < num_states; i++) {
		states[i] = (char *) malloc(sizeof(char) * hlen);
		memcpy(states[i], hello, hlen);
		
	}

	for (states_idx = 0; states_idx < num_states; states_idx++)
	{
		printf("state %d: %s\n", states_idx, states[states_idx]);
		free(states[states_idx]);
	}
	return 0;
}
