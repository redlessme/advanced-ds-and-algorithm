from z import mathPattern
from modified_kmp import KMP
from boyermoore import BM
# from testA1 import BM

# if __name__ == '__main__':
#     f = open("reference.txt","r")
#     txt = f.readline()
#
#     f.close()
#     f1=open("pattern-collection.txt","r")
#     compare=open("compare.txt",'w')
#     compare.write("Pattern\tZ\tBM\tKMP\t\n")
#     txt=txt.strip()
#     for pat in f1.readlines():
#         pat=pat.strip()
#
#         z=mathPattern(pat,txt)
#
#         bm=BM(txt,pat)
#
#         kmp=KMP(txt,pat)
#
#         compare.write("{}\t{}\t{}\t{}\n".format(pat,z[0],bm[0],kmp[0]))
#     compare.close()
if __name__ == '__main__':
    f = open("reference.txt","r")
    txt = f.readline()
    f.close()
    bm=[]
    kmp=[]
    z=[]
    f1=open("pattern-collection.txt","r")
    i=0
    txt=txt.strip()
    for pat in f1.readlines():
        pat=pat.strip()

        kmp.append(KMP(txt,pat))
        z.append((mathPattern(pat,txt)))
        bm.append((BM(txt,pat)))

    print(kmp==z)

    print("kmp",z[i]==kmp[i])
    print("bm",z[i]==bm[i])
    print(kmp==z==bm)

