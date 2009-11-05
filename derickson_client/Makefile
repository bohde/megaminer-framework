sources = $(wildcard *.cpp)
objects = $(sources:.cpp=.o)
deps = $(sources:.cpp=.d)
CPPFLAGS = -g

CPPFLAGS += -I. -Isexp

all: client

%.d: %.cpp
	@set -e; rm -f $@; \
	(dirname $< | tr '\n' '/'; $(CXX) -MM $(CPPFLAGS) $<) > $@.$$$$; \
	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
	rm -f $@.$$$$

.PHONY: clean all

clean:
	rm -f $(objects) $(deps) client
	$(MAKE) -C sexp clean

client: $(objects) sexp/sexp.a
	$(CXX) $(LDFLAGS) $(LOADLIBES) $(LDLIBS) $^ -g -o client

libclient.so: network.o game.o getters.o util.o sexp/sexp.a
	g++ -shared -Wl,-soname,libclient.so -o libclient.so network.o game.o getters.o util.o sexp/sexp.a

sexp/sexp.a:
	$(MAKE) -C sexp

-include $(deps)
