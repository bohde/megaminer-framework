sources = $(wildcard *.c)
objects = $(sources:%.c=%.o)
libclient_objects = $(sources:%.c=libclient_%.o)
deps = $(sources:%.c=%.d)

all: sexp.a libclient_sexp.a

clean:
	rm -f $(objects) $(libclient_objects) $(deps) sexp.a libclient_sexp.a

%.d: %.c
	@set -e; rm -f $@; \
	(dirname $< | tr '\n' '/'; $(CC) -MM $(CPPFLAGS) $<) > $@.$$$$; \
	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
	rm -f $@.$$$$

libclient_%.o: CFLAGS += -fPIC
libclient_%.o: %.c
	$(CC) -c $(CPPFLAGS) $(CFLAGS)   $< -o $@


.PHONY: sexp.a(PHONY) clean all

sexp.a(${objects}) sexp.a(PHONY): ${objects}
	ar cr sexp.a $^
	ranlib sexp.a

libclient_sexp.a(${libclient_objects}) libclient_sexp.a(PHONY): ${libclient_objects}
	ar cr libclient_sexp.a $^
	ranlib libclient_sexp.a

sexp.a: sexp.a(PHONY)
libclient_sexp.a: libclient_sexp.a(PHONY)

-include $(deps)

