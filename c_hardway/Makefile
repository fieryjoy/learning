CC=cc
CFLAGS=-Wall -g   

LD=$(CC)
LDFLAGS = -lm 

RM=rm

INCLS = $(wildcard *.h)
SRCS = $(wildcard *.c)
OBJS = $(patsubst %.c,%.o,$(SRCS))

all: $(OBJS) 

%.o: %.c 
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@

object.o: object.h object.c
	$(CC) $(CFLAGS) $(LDFLAGS) -c $^

ex19.o: object.o ex19.c ex19.h
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@

ex22.o: ex22.h ex22.c dbg.h
	$(CC) $(CFLAFS) $(LDFLAGS) -c $^

ex22_main.o: ex22.o ex22_main.c
	$(CC) $(CFLAFS) $(LDFLAGS) $^ -o $@

static.o: static.c static.h
	$(CC) $(CFLAFS) $(LDFLAGS) -c $^ 

static_main.o: static.o static_main.c
	$(CC) $(CFLAFS) $(LDFLAGS) $^ -o $@


clean:
	$(RM) $(OBJS) *.gch	
