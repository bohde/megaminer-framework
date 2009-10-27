JAVAFILES=$(shell ls *.java 2> /dev/null)

all: ../libclient.so Main.class

run: all
	LD_LIBRARY_PATH=.. java -cp jna.jar:. Main

../libclient.so: 
	make -C ../ libclient.so

Main.class: $(JAVAFILES) ../libclient.so
	javac -cp jna.jar:. $(JAVAFILES)


clean:
	rm -f *.class
	rm -f ../libclient.so
