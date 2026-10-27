# DUMB game: copy the named lumps from one WAD into another, keeping
# every other lump as it is and every lump 4-byte aligned (as
# libdumbwad's wadwr does).  Each name must occur exactly once in both WADs.
# Usage: patch-lumps.py BASE.wad FROM.wad OUT.wad NAME...
import struct
import sys


def read(path):
    d = open(path, 'rb').read()
    sig, n, off = struct.unpack('<4sii', d[:12])
    entries = [struct.unpack('<ii8s', d[off + 16 * i:off + 16 * i + 16])
               for i in range(n)]
    return sig, [(nm, d[o:o + sz]) for o, sz, nm in entries]


def name(nm):
    return nm.rstrip(b'\0').decode()


base, src, out_path, names = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
sig, lumps = read(base)
_, from_lumps = read(src)
for want in names:
    a = [i for i, (nm, _) in enumerate(lumps) if name(nm) == want]
    b = [data for nm, data in from_lumps if name(nm) == want]
    assert len(a) == 1 and len(b) == 1, want
    lumps[a[0]] = (lumps[a[0]][0], b[0])

out = bytearray(12)
directory = b''
for nm, data in lumps:
    while len(out) % 4:
        out += b'\0'
    directory += struct.pack('<ii8s', len(out), len(data), nm)
    out += data
while len(out) % 4:
    out += b'\0'
out[0:12] = struct.pack('<4sii', sig, len(lumps), len(out))
out += directory
open(out_path, 'wb').write(out)
