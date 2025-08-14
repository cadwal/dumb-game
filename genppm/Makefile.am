## Process this file with automake to produce Makefile.in

noinst_DATA = $(generated_ppms)
MOSTLYCLEANFILES = $(generated_ppms)

generated_ppms = sky_plan.ppm

# Generated pictures must already exist when the palette is built.
# That's why they have this directory of their own.  The texture
# directory also generates flipped images, but those use only the
# colors that are in the originals, so they don't matter.

sky_plan.ppm:
	$(PPMFORGE) -width 512 -height 150 -hour 16 >$@
