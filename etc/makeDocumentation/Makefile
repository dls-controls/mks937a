TOP = ../..
include $(TOP)/configure/CONFIG

# set to -d to get debugging
DEBUG :=

# this is the doxygen output dir
DOCDIR := $(TOP)/documentation/doxygen

# add the documentation files to the install target
install: $(DOCDIR)

# rule for creating the doxygen documentation
$(DOCDIR): config.src manual.src $(DOCDIR)/build_instructions_example
	mkdir -p $(DOCDIR)
	dls-make-doxygen-documentation.py -o $(DOCDIR) config.src manual.src

# rule for generating build instructions from an xml file
$(DOCDIR)/build_instructions_%: $(TOP)/etc/makeIocs/%.xml
	mkdir -p $(DOCDIR)
	dls-xml-iocbuilder.py --doc=$@ $(DEBUG) $^

# rule for generating build instructions from a py file
$(DOCDIR)/build_instructions_%: $(TOP)/etc/makeIocs/%.py
	mkdir -p $(DOCDIR)
	$^ --doc=$@ $(DEBUG) example

# don't do anything in clean
clean:

# Special rule to get rid of installed documentation dir
uninstall:
	$(RMDIR) $(DOCDIR)
