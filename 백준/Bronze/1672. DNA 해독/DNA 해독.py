n=int(input())
s=list(input())

dna = {"AA" : "A", "AG" : "C", "AC" : "A", "AT" : "G", "GA" : "C","GG" : "G",
       "GC" : "T", "GT" : "A", "CA" : "A", "CG" : "T", "CC" : "C", "CT" : "G",
       "TA" : "G", "TG" : "A", "TC" : "G","TT" : "T"}

while len(s) > 1:
    a = s.pop()
    b = s.pop()
    s.append(dna[b+a])

print(s[0])
