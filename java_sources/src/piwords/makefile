sourcefiles = \
 		AlphabetGenerator.java\
 		BaseTranslator.java\
 		DigitsToStringConverter.java \
 		PiGenerator.java \
 		WordFinder.java \
 		Main.java
 
classfiles  = $(sourcefiles:.java=.class)
#classfiles = Simple3.class Simple2.class Simple1.class
 
all: $(classfiles)
%.class: %.java
	javac -d . -classpath . $<
clean:
	rm -f *.class
