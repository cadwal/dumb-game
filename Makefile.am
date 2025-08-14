## Process this file with automake to produce Makefile.in

SUBDIRS = genppm palette pt sprite texture lvl

dumbdatadir = $(datadir)/dumb
dumbdata_DATA = game.wad

MOSTLYCLEANFILES = game.wad

EXTRA_DIST = wadinfo README.textures

palette_wad = palette/palette.wad
pt_wad = pt/pt.wad
texture_wad = texture/texture.wad
sprite_wad = sprite/sprite.wad
level_wads = $(srcdir)/lvl/E1M1.wad

subwads = $(palette_wad) $(pt_wad) $(texture_wad) $(sprite_wad)	\
$(level_wads)

game.wad: $(subwads) $(WADTOOL)
	$(WADTOOL) -W $@ \
	-f $(srcdir)/wadinfo \
	-c $(subwads)
