#MS VC: cl lpc21iap.c elf.c lpcusb.c libusb.lib

# Quiet compilation
Q=@

LIBNAME	= usb
APPNAME = lpc21iap

# Package definitions
PKG_NAME	= lpc21iap
DATE		= $$(date +%Y%m%d)
DATEL		= $$(date +%Y%m%d-%H%M)

# Tool definitions
<<<<<<< HEAD
CC      = gcc
=======
#joezie 2019/10/9
#CC = gcc
CC = $(MYCC)
#END joezie 2019/10/9
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
LD      = ld
AR      = ar
AS      = as
CP      = objcopy
OD		= objdump
RM		= rm
TAR		= tar

UNAME = $(shell uname -s)
ifeq ("$(UNAME)","Darwin")
  LIBRARYS = $(shell if test -d /opt/paparazzi/lib; then echo "-L/opt/paparazzi/lib"; elif test -d /opt/local/lib; then echo "-L/opt/local/lib"; fi)
  INCLUDES = $(shell if test -d /opt/paparazzi/include; then echo "-I/opt/paparazzi/include"; elif test -d /opt/local/include; then echo "-I/opt/local/include"; fi)
endif

CFLAGS  = -Wall -g -fPIC $(INCLUDES) $(LIBRARYS)

SOURCES =	lpc21iap.c elf.c lpcusb.c

all: $(APPNAME)

clean:
	$(Q)$(RM) -f core $(APPNAME).o $(APPNAME) $(APPNAME).obj $(APPNAME).exe

app: $(APPNAME)

<<<<<<< HEAD
$(APPNAME):	$(SOURCES) Makefile
	@echo LD $@
	$(Q)$(CC) $(CFLAGS) $(SOURCES) -o $(APPNAME) -l$(LIBNAME)
=======
#joezie 2019/10/8
#$(APPNAME):	$(SOURCES) Makefile
#	@echo LD $@
#	$(Q)$(CC) $(CFLAGS) $(SOURCES) -o $(APPNAME) -l$(LIBNAME)

$(APPNAME):	$(SOURCES) Makefile
	@echo "inn " $(shell pwd)
	@echo LD $@
	$(Q)$(MYCC) $(RULE) $(CFLAGS) $(SOURCES) -o $(APPNAME) -l$(LIBNAME)

#END joezie 2019/10/8
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3

# Builds archive tar file
arch: clean
	cd .. && $(TAR) --exclude={CVS,cvs} -cvzf $(PKG_NAME)-$(DATEL).tar.gz $(PKG_NAME)

# Builds release tar file
dist: clean
	cd .. && $(TAR) --exclude={CVS,cvs} -cvzf $(PKG_NAME)-$(DATE).tar.gz $(PKG_NAME)

.PHONY: all clean app arch dist
