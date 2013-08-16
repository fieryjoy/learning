#include <stdio.h>

void first_way_print(char *names[], int ages[], int count)
{
	int i = 0;

	for (i = 0; i < count; i++) {
		printf("%s has %d years alive.\n",
				names[i], ages[i]);
		printf("%p -> %s;  %p -> %d\n", 
				&names[i], names[i], &ages[i], ages[i]);
	}
}

void second_way_print(char **cur_name, int *cur_age, int count)
{
	int i = 0;
	// second way of using pointers
	for (i = 0; i < count; i++) {
		printf("%s is %d years old.\n", 
				*(cur_name+i), *(cur_age+1));

		printf("%p -> %s;  %p -> %d\n", 
				cur_name + i, *(cur_name + i), cur_age + i, *(cur_age + i));
	}
}

void third_way_print(char **cur_name, int *cur_age, int count)
{
	int i = 0;
	for (i = 0; i < count; i++) {
        printf("%s is %d years old.\n",
                cur_name[i], cur_age[1]);

        printf("%p -> %s;  %p -> %d\n",
                &cur_name[i], cur_name[i], &cur_age[i], cur_age[i]);
	}
}

void fourth_way_print(char *names[], int ages[], int count)
{
	char **cur_name;
	int *cur_age;
    for(cur_name = names, cur_age = ages;
            (cur_age - ages) < count;
            cur_name++, cur_age++)
    {
        printf("%s lived %d years so far.\n",
                *cur_name, *cur_age);
		printf("%p -> %s;  %p -> %d\n",
                cur_name, *cur_name, cur_age, *cur_age);
    }
}
	

int main(int argc, char *argv[])
{
	int ages[] = {23, 43, 12, 89, 2};
	char *names[] = {
		"Alan", "Frank",
		"Mary", "John", "Lisa"
	};

	// safely get the size of the ages
	int count = sizeof(ages) / sizeof(int);

	// first way using indexing
	first_way_print(names, ages, count);
	printf("---\n");

	second_way_print(names, ages, count);
	printf("---\n");
	
	third_way_print(names, ages, count);
	printf("---\n");

	fourth_way_print(names, ages, count);
	return 0;
}

