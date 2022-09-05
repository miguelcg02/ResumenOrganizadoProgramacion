l = input()
l=list(l)
n=int(l[0]) # Numero de entradas
k=int(l[2]) # Max
nu=list(input())
nums = []
# k = 7
# nums=[8,2,2,3] # arreglo de numeros

i=0
while i<= len(nu):
    nums.append(int(nu[i]))
    i+=2

# def sumaGrupos(i,nums,k) -> bool:
#     if i==len(nums):
#         return 'YES'
#     else:
#         sumaGrupos(i+1,nums,k) or sumaGrupos(i+1,nums,k-nums[i])
#         return 'YES'

def sumaGrupos(i,nums,k):
    if k == 0:
        return True
    if i>=len(nums):
        return False
    a = sumaGrupos(i+1,nums,k) or sumaGrupos(i+1,nums,k-nums[i])
    return a

f = sumaGrupos(0,nums,k)
if f==True:
    print("YES")
else:
    print("NO")