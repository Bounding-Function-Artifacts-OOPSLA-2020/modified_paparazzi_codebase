Q=@
<<<<<<< HEAD
CC = gcc
=======

#joezie 2019/10/9
#CC = gcc
CC = $(MYCC)
#END joezie 2019/10/9
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3

TARGET = bluegiga_usb_driver

MACHINE = $(shell $(CC) -dumpmachine)
# Windows
ifneq (,$(or $(findstring mingw, $(MACHINE)), $(findstring cygwin, $(MACHINE))))
	PLATFORM = WIN
	LIBS = -lm -lsetupapi
	RM = del
# POSIX
else
	PLATFORM = POSIX
	LIBS = -lm -lpthread
endif

SRCS := $(wildcard *.c)
OBJS := $(SRCS:.c=.o)
DEPS := $(SRCS:.c=.d)

all: $(TARGET)

<<<<<<< HEAD
%.o: %.c
	$(Q)$(CC) -O3 -Wall -c -fmessage-length=0 -DPLATFORM_$(PLATFORM) -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o"$@" "$<"

$(TARGET): $(OBJS)
	@echo 'Building target: $@'
	$(Q)$(CC) -o $(TARGET) $(OBJS) $(LIBS)
	@echo 'Finished building target: $@'
=======
#joezie 2019/10/8

#%.o: %.c
#	$(Q)$(CC) -O3 -Wall -c -fmessage-length=0 -DPLATFORM_$(PLATFORM) -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o"$@" "$<"

#$(TARGET): $(OBJS)
#	@echo 'Building target: $@'
#	$(Q)$(CC) -o $(TARGET) $(OBJS) $(LIBS)
#	@echo 'Finished building target: $@'

%.o: %.c
	@echo "inn " $(shell pwd)
	$(Q)$(MYCC) $(RULE) -O3 -Wall -c -fmessage-length=0 -DPLATFORM_$(PLATFORM) -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o"$@" "$<"

$(TARGET): $(OBJS)
	@echo 'Building target: $@'
	$(Q)$(CC) -o $(TARGET) -no-pie $(OBJS) $(LIBS)
	@echo 'Finished building target: $@'
		
#END joezie 2019/10/8
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3

clean:
	-$(RM) $(OBJS) $(DEPS) $(TARGET)

.PHONY: all clean
