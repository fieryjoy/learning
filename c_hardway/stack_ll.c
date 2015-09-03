#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct stack {
	int data;
	struct stack *next;
} STACK;

int is_empty(STACK *head)
{
	return (head == NULL); 		
}

int top(STACK *head)
{
	return head->data;
}

void init(STACK **head)
{
	*head = NULL;
}

void push(STACK **head, int value)
{
	STACK *node = malloc(sizeof(STACK));           /* create a new node */

	if (node == NULL) {
		fputs("Error: no space available for node\n", stderr);
		abort();
	} else {
		node->data = value;                        /* initialize node */
		node->next = is_empty(*head) ? NULL : *head;  /* insert new head if any */
		*head = node;
	}
}

int pop(STACK **head)
{
	if (is_empty(*head)) {                             /* stack is empty */
		fputs("Error: stack underflow\n", stderr);
		abort();
	} else {                                        // pop a node
		STACK *top = *head;
		int value = top->data;
		*head = top->next;
		free(top);
		return value;
	}
}

void outputInBinary(int n)
{
	STACK *head;

	init(&head);
	printf("%d in binary is: ", n);
	while (n > 0) 
	{
		int bit = n % 2;
		push(&head, bit);
		n = n / 2;
	}
	while (!is_empty(head)) 
	{
		printf("%d", pop(&head));
	}
	printf("\n");
}

void TowersofHanoi(int n, int a, int b, int c)
{
	if (n > 0)
	{
		TowersofHanoi(n-1, a, c, b);
		printf("> Move top disk from tower %d to tower %d.\n", a, b);
		TowersofHanoi(n-1, c, b, a);
	}
}


int main(int argc, char *argv[])
{
	int i;
	for (i = 0; i < 1024; i++)
	{
		outputInBinary(i);
	}

	TowersofHanoi(5, 1,2,3);
/*
	STACK *head;
	int i;
	init(&head);
	printf("%s\n", is_empty(head)?"empty":"non-empty");
	for (i = 0; i < 100000; i++)
	{
		push(&head, i);
	}
	printf("%s\n", is_empty(head)?"empty":"non-empty");
	printf("The TOP: %d\n", top(head));
	printf("%d\n", pop(&head));
	printf("%d\n", pop(&head));
	printf("%s\n", is_empty(head)?"empty":"non-empty");
	printf("The TOP: %d\n", top(head));
	while (!(is_empty(head))) {
		printf("%d\n", pop(&head));
	}
	printf("%s\n", is_empty(head)?"empty":"non-empty");
*/	
	return 0;
}
