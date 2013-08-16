CC=cc
CFLAGS=-Wall -g   

LD=$(CC)
LDFLAGS = -lm 

RM=rm

INCLS = $(wildcard *.h)
SRCS = $(wildcard *.c)
OBJS = $(patsubst %.c,%.o,$(SRCS))

all: $(OBJS) 

object.o: object.h object.c
	$(CC) -c object.h object.c

ex19.o: object.o ex19.c ex19.h
	$(CC) $(CFLAGS) $^ -o $@

%.o: %.c %.h
	$(CC) $(CFLAGS) $(LDFLAGS) $< -o $@


clean:
	$(RM) $(OBJS)	
