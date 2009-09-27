all: sexpbuild


sexpbuild: cstring.o sexp.o event_temp.o faststack.o io.o parser.o sexp_memory.o sexp_ops.o sexp_vis.o cstring.h  faststack.h  sexp_errors.h  sexp.h  sexp_memory.h  sexp_ops.h  sexp_vis.h
	touch sexpbuild

sexp.o: cstring.h  faststack.h  sexp_errors.h  sexp.h  sexp_memory.h  sexp_ops.h  sexp_vis.h
	g++ -g sexp.c -c -fPIC

cstring.o: cstring.h  faststack.h  sexp_errors.h  sexp.h  sexp_memory.h  sexp_ops.h  sexp_vis.h
	g++ -g cstring.c -c -fPIC

event_temp.o: cstring.h  faststack.h  sexp_errors.h  sexp.h  sexp_memory.h  sexp_ops.h  sexp_vis.h
	g++ -g event_temp.c -c -fPIC

faststack.o: cstring.h  faststack.h  sexp_errors.h  sexp.h  sexp_memory.h  sexp_ops.h  sexp_vis.h
	g++ -g faststack.c -c -fPIC

io.o: cstring.h  faststack.h  sexp_errors.h  sexp.h  sexp_memory.h  sexp_ops.h  sexp_vis.h
	g++ -g io.c -c -fPIC

parser.o: cstring.h  faststack.h  sexp_errors.h  sexp.h  sexp_memory.h  sexp_ops.h  sexp_vis.h
	g++ -g parser.c -c -fPIC

sexp_memory.o: cstring.h  faststack.h  sexp_errors.h  sexp.h  sexp_memory.h  sexp_ops.h  sexp_vis.h
	g++ -g sexp_memory.c -c -fPIC

sexp_ops.o: cstring.h  faststack.h  sexp_errors.h  sexp.h  sexp_memory.h  sexp_ops.h  sexp_vis.h
	g++ sexp_ops.c -c -fPIC

sexp_vis.o: cstring.h  faststack.h  sexp_errors.h  sexp.h  sexp_memory.h  sexp_ops.h  sexp_vis.h
	g++ sexp_vis.c -c -fPIC

clean:
	rm -f *.o sexpbuild
