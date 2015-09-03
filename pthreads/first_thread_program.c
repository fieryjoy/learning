#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define NUM_THREADS 5

struct thread_data {
	int thread_id;
	int sum;
	char *message;
};

struct thread_data thread_data_array[NUM_THREADS];

void *PrintHello(void *threadarg)
{
	struct thread_data *my_data;
	int taskid;
	int sum;
	char *hello_msg;

	my_data = (struct thread_data *) threadarg;
	taskid = my_data->thread_id;
	sum = my_data->sum;
	hello_msg = my_data->message;

	printf("%s #%d! Sum is: %d\n", hello_msg, taskid, sum);
	
	pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
	pthread_t threads[NUM_THREADS];	
	char * messages[NUM_THREADS] = {};	
	int rc;
	int t = 0;
	int sum = 10;	

	for (t = 0; t < NUM_THREADS; t++) {		
		printf("In main: creating thread %d\n", t);
		
		messages[t] = "Hello World! It's me, thread";
		thread_data_array[t].thread_id = t;
		thread_data_array[t].sum = sum;
		thread_data_array[t].message = messages[t];

		sum += 1;

		rc = pthread_create(&threads[t], NULL, PrintHello, (void *) &thread_data_array[t]);
		if (rc) {
			printf("ERROR: return code from pthread_create() is %d\n", rc);
			exit(-1);
		}
	}
	
	/* Last thing that main() should do */
	pthread_exit(NULL);
}
