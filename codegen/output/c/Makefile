sources = $(wildcard *.cpp)
objects = $(sources:.cpp=.o)
deps = $(sources:.cpp=.d)

CPPFLAGS += -I. -Isexp

all: main

%.d: %.cpp
	@set -e; rm -f $@; \
	(dirname $< | tr '\n' '/'; $(CXX) -MM $(CPPFLAGS) $<) > $@.$$$$; \
	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
	rm -f $@.$$$$

.PHONY: clean all

clean:
	rm -f $(objects) $(deps)
	$(MAKE) -C sexp clean

main: $(objects) sexp/sexp.a
	$(CXX) $(LDFLAGS) $(LOADLIBES) $(LDLIBS) $^ -o main

sexp/sexp.a:
	$(MAKE) -C sexp

-include $(deps)
