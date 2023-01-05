#sorting algorithm in normal python

nt=int(input("Enter number of teachers:"))
d={}
for i in range(0,nt,1):
  s={}
  t=input("Enter teacher name:")
  g=int(input("Enter number of grades taught:"))
  for  j in range(0,g,1):
    gr=int(input())
    sj=input("Enter subject name:")
    s[gr]=sj
  d[t]=s  
p=int(input("Enter number of periods:"))
np=int(input("Enter lunch period number:"))
pt=int(input("Enter number of minutes taken for 1 period:"))

