#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NTHREADS 4
#define N 10
#define MEGEXTRA 16284


pthread_attr_t attr;

void printA(double A[N][N])
{
	int i,j;
	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			printf("A[%d][%d] = %f\n", i, j, A[i][j]);
}

void *dowork(void *threadid)
{
	double A[N][N];
	int i,j;
	long tid;
	size_t mystacksize;

	tid = (long)threadid;
	pthread_attr_getstacksize(&attr, &mystacksize);
	printf("Thread %ld: stack size = %li bytes \n", tid, (long int)mystacksize);
	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			A[i][j] = ((i*j)/3.452) + (N - 1);
	printA(A);	
	pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
	pthread_t threads[NTHREADS];
	size_t stacksize;
	int rc;
	long t;

	pthread_attr_init(&attr);
	pthread_attr_getstacksize(&attr, &stacksize);
	printf("Default stack size = %li\n", (long)stacksize);
	stacksize = sizeof(double) * N * N + MEGEXTRA;
	printf("Amount of stack needed per thread = %li\n", (long)stacksize);
	rc = pthread_attr_setstacksize(&attr, stacksize);
	if (rc) 
	{
		printf("ERROR: return code from pthread_attr_setstacksize() is %s\n", strerror(rc));
		exit(-1);
	}
	printf("Creating threads with stack size = %li bytes\n", (long)stacksize);
	for (t = 0; t < NTHREADS; t++) 
	{
		rc = pthread_create(&threads[t], &attr, dowork, (void *)t);
		if (rc) 
		{
			printf("ERROR: return code from pthread_create() is %d\n", rc);
			exit(-1);
		}
	}
	printf("Created %ld threads.\n", t);
	pthread_exit(NULL);
}
