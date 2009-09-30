sources = $(wildcard *.c)
objects = $(sources:.c=.o)
deps = $(sources:.c=.d)

all: sexp.a

clean:
	rm -f $(objects) $(deps)

%.d: %.c
	@set -e; rm -f $@; \
	(dirname $< | tr '\n' '/'; $(CC) -MM $(CPPFLAGS) $<) > $@.$$$$; \
	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
	rm -f $@.$$$$

.PHONY: sexp.a(PHONY) clean all

sexp.a(${objects}) sexp.a(PHONY): ${objects}
	ar cr sexp.a ${objects}
	ranlib sexp.a

sexp.a: sexp.a(PHONY)

-include $(deps)

