#include <stdlib.h>
#include <stdio.h>

#define STACKSIZE 10

typedef struct {
	size_t size;
	int items[STACKSIZE];
} STACK;

STACK* init(STACK *ps)
{
	ps->size = 0;
	return ps;
}

int is_empty(STACK *ps)
{
	return (ps->size == 0);
}

STACK* push (STACK *ps, int x)
{
	if (ps->size == STACKSIZE) {
		fputs("Error: stack overflow\n", stderr);
		abort();
	} else
		ps->items[ps->size++] = x;
	return ps;
}

int pop(STACK *ps)
{
	if (is_empty(ps)) {
		fputs("Error: stack underflow\n", stderr);
		abort();
	} else
		return ps->items[--ps->size];
}

int top(STACK *ps) 
{
	int last;
	if (is_empty(ps)) {
		fputs("Error: stack underflow\n", stderr);
		abort();
	} else
		{
			last = ps->size - 1;
			return ps->items[last];
		}
}

int main(int argc, char *argv[]) 
{
	STACK stack;
	int i;

	init(&stack);	
//	top(init(&stack));
	printf("AFTER INIT: %s\n", is_empty(&stack)? "empty" : "non empty");
	
	for (i = 0; i < 20; i++)
	{
		push(&stack, i);
	}
	printf("THE TOP: %d\n", top(&stack));
		
	printf("AFTER PUSH: %s\n", is_empty(&stack)? "empty" : "non empty");

	printf("%d\n", pop(&stack));
	printf("%d\n", pop(&stack));
	printf("%d\n", pop(&stack));
	printf("%d\n", pop(&stack));

	printf("AFTER POPS:\n");	
	for (i = 0; i < stack.size; i++)
	{
		printf("%d\n", stack.items[i]);
	}
	return 0;
}

