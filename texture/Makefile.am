## Process this file with automake to produce Makefile.in

noinst_DATA = $(texture_wad)

MOSTLYCLEANFILES = $(built_ppms) \
 $(flat_lumps) $(patch_lumps) $(pname_lumps) \
 $(texture_wad)

EXTRA_DIST = pnames \
 brikflor.ppm fplnk.ppm gargoyle.ppm ice.ppm lbrkflor.ppm \
 lilbrick.ppm lplnk.ppm rockflor.ppm rufbrick.ppm stonwalb.ppm \
 stonwals.ppm tiles1.ppm whmarb.ppm woodflor.ppm woodflo2.ppm


palette = ../palette/palette.ppm
playpal = ../palette/PLAYPAL.lump

texture_wad = texture.wad

built_ppms = fplnk.r.ppm lplnk.r.ppm sky_plan.ppm

patch_lumps = gargoyle.patch lilbrick.patch lplnk.patch lplnk.r.patch \
 rockflor.patch rufbrick.patch stonwalb.patch stonwals.patch \
 sky_plan.patch

flat_lumps = brikflor.flat fplnk.flat fplnk.r.flat ice.flat lbrkflor.flat \
 rockflor.flat tiles1.flat whmarb.flat woodflor.flat woodflo2.flat

# PNAMES.lump must come before TEXTURE1.lump because the value of this
# variable is fed straight to $(MKPNAMES).
pname_lumps = PNAMES.lump TEXTURE1.lump


# Put patches before flats, so that if there are lumps with identical
# names, the patch will be found.  Flats are only searched between
# F_START and F_END anyway.
$(texture_wad): $(patch_lumps) $(flat_lumps) $(pname_lumps) $(WADTOOL)
	$(WADTOOL) -w $@ \
	-L P_START -f $(patch_lumps) -L P_END \
	-L F_START -f $(flat_lumps)  -L F_END \
	-f $(pname_lumps)


%.flat: %.ppm $(palette) $(playpal) $(PPMTODUMB)
	$(PPMQUANT) -fs -map $(palette) $< \
	| $(PPMTODUMB) -f -M $(playpal) >$@

%.patch: %.ppm $(palette) $(playpal) $(PPMTODUMB)
	$(PPMQUANT) -fs -map $(palette) $< \
	| $(PPMTODUMB) -p -M $(playpal) >$@

$(pname_lumps): pnames $(MKPNAMES)
	$(MKPNAMES) $< $(pname_lumps)

# Generated ppm files

%.r.ppm: %.ppm
	$(PNMFLIP) -ccw $< >$@

# TODO: Use a symbolic link.
sky_plan.ppm: ../genppm/sky_plan.ppm
	cp $< $@
