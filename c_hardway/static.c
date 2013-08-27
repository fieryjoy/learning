#include "static.h"
#include <stdio.h>

int *pcount = 0;

int hello()
{
	static int count = 5;
	if (pcount == NULL)
	{
		pcount = &count;
	}
	count++;
	return count;
}


