## Process this file with automake to produce Makefile.in

noinst_DATA = $(palette_wad) palette.ppm PLAYPAL.lump

MOSTLYCLEANFILES = $(colormap_lumps) $(palette_wad)
CLEANFILES = pal-nt.ppm pal-tail.ppm palette.ppm PLAYPAL.lump

palette_wad = palette.wad
colormap_lumps = COLORMAP.lump COLORM16.lump COLORM32.lump

all_pictures = ../genppm/*.ppm \
 $(top_srcdir)/sprite/*.ppm \
 $(top_srcdir)/texture/*.ppm

$(palette_wad): PLAYPAL.lump $(colormap_lumps) $(WADTOOL)
	$(WADTOOL) -w $@ \
	-f PLAYPAL.lump $(colormap_lumps)

PLAYPAL.lump: palette.ppm $(PPMTODUMB)
	$(PPMTODUMB) -m <$< >$@

COLORMAP.lump: PLAYPAL.lump $(PPMTODUMB)
	$(PPMTODUMB) -c -M $< >$@

COLORM16.lump: PLAYPAL.lump $(PPMTODUMB)
	$(PPMTODUMB) -c -2 -M $< >$@

COLORM32.lump: PLAYPAL.lump $(PPMTODUMB)
	$(PPMTODUMB) -c -4 -M $< >$@


palette.ppm: pal-nt.ppm pal-tail.ppm
	$(PNMCAT) -lr $^ >$@

pal-nt.ppm:
	$(PNMCAT) -tb $(all_pictures) \
	| $(PPMQUANT) 255 \
	| $(PPMTOMAP) \
	| $(PPMCHANGE) "#000001" "#000000" \
	| $(PNMDEPTH) 255 >$@

pal-tail.ppm:
	$(PPMMAKE) "#000001" 1 1 | $(PNMDEPTH) 255 >$@
