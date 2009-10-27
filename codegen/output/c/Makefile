sources = $(wildcard *.cpp)
objects = $(sources:%.cpp=%.o)
deps = $(sources:%.cpp=%.d)
CPPFLAGS = -DSHOW_NETWORK -g

CPPFLAGS += -I. -Isexp

all: client libclient.so

%.d: %.cpp
	@set -e; rm -f $@; \
	(dirname $< | tr '\n' '/'; $(CXX) -MM $(CPPFLAGS) $<) > $@.$$$$; \
	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
	rm -f $@.$$$$

.PHONY: clean all

libclient_%.o: CXXFLAGS += -fPIC
libclient_%.o: %.cpp %.d
	$(CC) -c $(CPPFLAGS) $(CXXFLAGS) $< -o $@

clean:
	rm -f $(objects) $(deps) client libclient.so
	$(MAKE) -C sexp clean

client: $(objects) sexp/sexp.a
	$(CXX) $(LDFLAGS) $(LOADLIBES) $(LDLIBS) $^ -g -o client

libclient.so: libclient_network.o libclient_game.o libclient_getters.o libclient_util.o sexp/libclient_sexp.a
	$(CXX) -shared -Wl,-soname,libclient.so $(LDFLAGS) $(LOADLIBES) $(LDLIBS) $^ -o libclient.so

sexp/sexp.a sexp/libclient_sexp.a:
	$(MAKE) -C sexp

-include $(deps)
