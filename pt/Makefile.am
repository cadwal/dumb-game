## Process this file with automake to produce Makefile.in

noinst_DATA = $(pt_wad)
MOSTLYCLEANFILES = $(pt_lumps) $(pt_wad)
EXTRA_DIST = $(pt_sources)

pt_sources = game.pt creatures.pt decoration.pt generic.pt levels.pt \
 linetypes.pt missiles.pt weapons.pt

pt_lumps = ANIMTEX.lump GETTABLE.lump LEVINFO.lump LINETYPE.lump PHASES.lump \
 PROTOS.lump SECTTYPE.lump SOUNDS.lump

pt_wad = pt.wad

pt_preprocess = $(CXXCPP) -x c-header -I$(srcdir)

$(pt_wad): $(pt_lumps) $(WADTOOL)
	$(WADTOOL) -w $@ \
	-f $(pt_lumps)

$(pt_lumps): $(pt_sources) $(PTCOMP)
	$(pt_preprocess) $(srcdir)/game.pt | $(PTCOMP) .
