# %s(string), %d(int), %b(bool), %f(float)
a=134
b="cachorro"
c=12.3

print("O valor de a é %d, e o valor de b é %s, já o valor de c é %f" %(a,b,c))
print("O valor de c é %.2f"%(c)) # Para definir as casas decimais, colocar (.+o número de casas decimais) depois da porcentagem e antes do f.
print("O valor de c é {:.2f}".format(c)) #É uma outra forma, usando a função .format(var)