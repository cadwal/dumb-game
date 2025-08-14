## Process this file with automake to produce Makefile.in

noinst_DATA = $(sprite_wad)

MOSTLYCLEANFILES = $(sprite_lumps) $(sprite_wad)

EXTRA_DIST = fbala0.ppm fbalb0.ppm fbalc0.ppm fbald0.ppm fbale0.ppm \
 fbalf0.ppm fbalg0.ppm newsa0.ppm


palette = ../palette/palette.ppm
playpal = ../palette/PLAYPAL.lump

sprite_wad = sprite.wad

sprite_lumps = fbala0.patch fbalb0.patch fbalc0.patch fbald0.patch \
 fbale0.patch fbalf0.patch fbalg0.patch newsa0.patch


$(sprite_wad): $(sprite_lumps) $(WADTOOL)
	$(WADTOOL) -w $@ \
	-L S_START -f $(sprite_lumps) -L S_END


%.patch: %.ppm $(palette) $(playpal) $(PPMTODUMB)
	$(PPMQUANT) -fs -map $(palette) $< \
	| $(PPMTODUMB) -p -M $(playpal) >$@
