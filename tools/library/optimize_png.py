import sys,os,re
from PIL import Image
from multiprocessing import Pool
D=(sys.argv[1].rstrip('/')+'/icons') if len(sys.argv)>1 else '.'
def q(f):
    im=Image.open(f).convert('RGBA'); a=im.getchannel('A')
    p=im.quantize(colors=64,method=Image.Quantize.FASTOCTREE,dither=Image.Dither.NONE)
    p.save(f,'PNG',optimize=True); return os.path.getsize(f)
if __name__=='__main__':
    fs=[f for f in [os.path.join(D,x) for x in os.listdir(D)] if re.search(r'-(on|off)(-clear)?\.png$',f)]
    with Pool(2) as pool: s=sum(pool.map(q,fs,chunksize=200))
    print(len(fs),s/1048576)
