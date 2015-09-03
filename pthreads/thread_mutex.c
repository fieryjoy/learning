#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

/* The following structure contains the necessary information 
to allow the function "dotprod" to access its input data and
place its output into the structure.
*/

typedef struct 
{
	double *a;
	double *b;
	double sum;
	int veclen;
} DOTDATA;

/* define globally accessible variables and a mutex */

#define VECLEN 100
#define NUMTHRDS 4

DOTDATA dotstr;

pthread_t callThd[NUMTHRDS];
pthread_mutex_t mutexsum;


/*
The function dotprod is activated when the thread is created.
All input to this routine is obtained from a structure
of type DOTDATA and all output from this function is written into
this structure. The benefit of this approach is apparent for the 
multi-threaded program: when a thread is created we pass a single
argument to the activated function - typically this argument
is a thread number. All the other information required by the 
function is accessed from the globally accessible structure.
*/

void *dotprod(void *arg)
{
	/* Define and use local variables for convenience */

	int start, end, i, len;
	long offset;
	double mysum, *x, *y;
	offset = (long)arg;
	
	len = dotstr.veclen;
	start = offset * len;
	end = start + len;
	x = dotstr.a;
	y = dotstr.b;

	/* Perform the dot product and assign result 
	to the appropriate variable in the structure.
	 */	

	mysum = 0;
	for (i = start; i < end; i++)
	{
		mysum += (x[i] * y[i]);
	}

	/* Lock a mutex prior to updating the value in the shared 
	structure, and unlock it upon updating.
	*/
	pthread_mutex_lock(&mutexsum);
	dotstr.sum = mysum;
	printf("Thread %ld did %d to %d:  mysum=%f global sum=%f\n",offset,start,end,mysum,dotstr.sum);
	pthread_mutex_unlock(&mutexsum);

	pthread_exit((void *) 0);
}

int main(int argc, char *argv[])
{
	long i;
	double *a, *b;
	void *status;
	pthread_attr_t attr;

	/* Assign storage and initialize values */
	a = (double *) malloc (NUMTHRDS*VECLEN*sizeof(double));
	b = (double *) malloc (NUMTHRDS*VECLEN*sizeof(double));

	for (i = 0; i < VECLEN*NUMTHRDS; i++)
	{
		a[i] = 1.0;
		b[i] = a[i];
	}

	dotstr.veclen = VECLEN;
	dotstr.a = a;
	dotstr.b = b;
	dotstr.sum = 0;

	pthread_mutex_init(&mutexsum, NULL);
	/* Create threads to perform the dotproduct */
	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

	for (i = 0; i < NUMTHRDS; i++)
	{
		pthread_create(&callThd[i], &attr, dotprod, (void *) i);
	}

	pthread_attr_destroy(&attr);

	/* Wait for the other threads */
	for (i = 0; i < NUMTHRDS; i++)
	{
		pthread_join(callThd[i], &status);
	}


	printf("Sum = %f \n", dotstr.sum);
	free(a);
	free(b);
	pthread_mutex_destroy(&mutexsum);
	pthread_exit(NULL);
	return 0;
}
