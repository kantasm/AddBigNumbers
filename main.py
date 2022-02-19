b = '999999436546456546654645645645645654654654645654645645654654653454353499'
a = '15654644645645645645564565465464564565464565465464564565465645456654564'
c = int(a) + int(b)

sum1 = []
sum2 = []

if len(a) < len(b):
  s=a
  a=b
  b=s

sum1 = a[::-1]
sum2 = b[::-1]

x=len(a)-len(b)
z='0'*x
sum2=sum2+z

#print(sum1,sum2)

alen = len(sum1)
blen = len(sum2)

sum3=''
carry=0
i=0
while i <= blen - 1:
    sum4 = int(sum1[i])+int(sum2[i])+carry
    #print('sum4=',sum4)
    sum3 += str(sum4%10)
    #print('sum3=',sum3)
    carry = int((sum4 - sum4%10) / 10)
    #print(  sum3 + str(carry))
    i+=1

if carry > 0:
  sum3 = sum3 + str(carry)
sum3 = sum3[::-1]
print('result:',int(sum3)==c)
