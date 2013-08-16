CC=cc
CFLAGS=-Wall -g   

LD=$(CC)
LDFLAGS = -lm -pthread

RM=rm

SRCS = $(wildcard *.c)
OBJS = $(patsubst %.c,%.o,$(SRCS))

all: $(OBJS) 

%.o: %.c
	$(CC) $(CFLAGS) $(LDFLAGS) $< -o $@

clean:
	$(RM) $(OBJS)	
