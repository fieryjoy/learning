#include <stdio.h>
#include <stdarg.h>

void foo(char *fmt, ...)
{
	va_list ap;
	int d;
	char c, *s;
	double f;
	
	va_start(ap, fmt);
	while(*fmt)
		switch (*fmt++) {
			case 's':
				s = va_arg(ap, char *);
				printf("string %s\n", s);
				break;
			case 'd':
				d = va_arg(ap, int);
				printf("int %d\n", d);
				break;
			case 'c':
				c = (char) va_arg(ap, int);
				printf("char %c\n", c);
				break;
			case 'f': 
				f = va_arg(ap, double);
				printf("float %.2f\n", f);
				break;
		}
	va_end(ap);
}

int main(int argc, char *argv[])
{
	int distance = 100;
	float power = 2.345f;
	double super_power = 56789.4532;
	char initial = 'A';
	char first_name[] = "Zed";
	char last_name[] = "Shaw";

	printf("You are %d miles away.\n", distance);
	printf("You have %f levels of power.\n", power);
	printf("You have %10.2f awesome super powers.\n", super_power);
	printf("I have an initial %c.\n", initial);
	printf("I have a first name %s.\n", first_name);
	printf("I have a second name %s.\n", last_name);
	printf("My whole name is %s %c. %s.\n", first_name, initial, last_name);
	foo("sdccsddf", "hello", 5, 'A', 'B', "goodies", 6, 8, 5.6);	
	return 0;
}
