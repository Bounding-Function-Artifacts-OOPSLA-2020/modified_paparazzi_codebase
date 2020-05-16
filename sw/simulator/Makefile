# Hey Emacs, this is a -*- makefile -*-
#
# Copyright (C) 2003-2006  Pascal Brisset, Antoine Drouin
#
# This file is part of paparazzi.
#
# paparazzi is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# paparazzi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with paparazzi; see the file COPYING.  If not, write to
# the Free Software Foundation, 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

# Quiet compilation
Q=@


include ../../conf/Makefile.local
include ../Makefile.ocaml

OCAMLC += -g
INCLUDES =
PKG = -package glibivy,pprz
LINKPKG = $(PKG) -linkpkg -dllpath-pkg pprz,pprzlink

<<<<<<< HEAD
SIMML = simlib.ml data.ml flightModel.ml gps.ml
=======
SIMML = stdlib.ml data.ml flightModel.ml gps.ml
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
SIMHML = $(SIMML) hitl.ml sim.ml
SIMHCMO=$(SIMHML:%.ml=%.cmo)
SIMSML = $(SIMML) sitl.ml sim.ml
SIMSCMO=$(SIMSML:%.ml=%.cmo)
SIMSCMX=$(SIMSML:%.ml=%.cmx)

AIRBORNE = ../airborne
VARINCLUDE=$(PAPARAZZI_HOME)/var/include
ACINCLUDE = $(PAPARAZZI_HOME)/var/$(AIRCRAFT)

CAML_CFLAGS = -I $(shell $(OCAMLC) -where)


all : gaia sitl.cma

sitl.cma : fg.o $(SIMSCMO) $(LIBPPRZCMA) $(LIBPPRZLINKCMA)
	@echo OL $@
	$(Q)$(OCAMLMKLIB) -o sitl $^

sitl.cmxa : $(SIMSCMX) $(LIBPPRZCMXA) $(LIBPPRZLINKCMXA)
	@echo OC $@
	$(Q)$(OCAMLOPT) -o $@ -a $^

gaia : gaia.cmo $(LIBPPRZCMA) $(LIBPPRZLINKCMA)
	@echo OL $@
	$(Q)$(OCAMLC) $(INCLUDES) -o $@ $(LINKPKG) gtkInit.cmo $<

<<<<<<< HEAD
diffusion : simlib.cmo diffusion.cmo
=======
diffusion : stdlib.cmo diffusion.cmo
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
	@echo OL $@
	$(Q)$(OCAMLC) $(INCLUDES) -o $@ $(LINKPKG) gtkInit.cmo $^

%.cmo : %.ml
	@echo OC $<
	$(Q)$(OCAMLC) $(INCLUDES) -c $(PKG) $<

<<<<<<< HEAD
%.o : %.c
	@echo CC $<
	$(Q)$(CC) -fPIC -c $< $(CAML_CFLAGS)
=======
#joezie 2019/10/8
#%.o : %.c
#	@echo CC $<
#	$(Q)$(CC) -fPIC -c $< $(CAML_CFLAGS)

%.o : %.c
	@echo CC $<
	$(Q)$(MYCC) $(RULE) -fPIC -c $< $(CAML_CFLAGS)

#END joezie 2019/10/8
>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3

%.cmx : %.ml
	@echo OOC $<
	$(Q)$(OCAMLOPT) $(INCLUDES) -c $(PKG) $<

%.cmi : %.mli
	@echo OC $<
	$(Q)$(OCAMLC) $(INCLUDES) -c $(PKG) $<

<<<<<<< HEAD
=======
nps_sensor_accel.o : nps/nps_sensor_accel.c
	@echo CC $<
	$(Q)$(CC) -g -O2 -Wall $(shell pkg-config gtk+-2.0 --cflags) -fPIC -c $< $(CAML_CFLAGS) $(shell pkg-config gtk+-2.0 --libs) -s -lglibivy -lm -lpcre
	#@echo clang $<
	#$(Q)clang -fPIC -emit-ast $< $(CAML_CFLAGS)

>>>>>>> 5926b573a907e168704d2426ee3d50a02e32d1b3
clean :
	$(Q)rm -f *.cm* *~ *.out .depend *.o *.a *.so gaia simhitl diffusion

.PHONY: all clean


#
# Dependencies
#

.depend: Makefile
	@echo DEPEND $@
	$(Q)$(OCAMLDEP) -I $(LIBPPRZDIR) *.ml* > .depend

ifneq ($(MAKECMDGOALS),clean)
-include .depend
endif
