## Process this file with automake to produce Makefile.in

noinst_DATA = $(pt_wad)
MOSTLYCLEANFILES = $(pt_wad) $(cpp_input)
EXTRA_DIST = $(pt_sources)

# Because it is only portable to run $(CXXCPP) on files with a `.c',
# '.C', or '.cc' extension, we create a temporary .cc file which just
# #includes the real input file.
cpp_input = temp.cc

pt_sources = game.pt creatures.pt decoration.pt generic.pt levels.pt	\
linetypes.pt missiles.pt weapons.pt

pt_wad = pt.wad

pt_preprocess = $(CXXCPP) -I$(srcdir)

# ptcomp writes all the lumps it knows about straight into a WAD.
$(pt_wad): $(pt_sources) $(PTCOMP)
	echo '/* This file is supposed to be deleted automatically. */' >$(cpp_input)
	echo '#include "$(srcdir)/game.pt"' >>$(cpp_input)
	$(pt_preprocess) $(cpp_input) | $(PTCOMP) -o $@
	rm $(cpp_input)
