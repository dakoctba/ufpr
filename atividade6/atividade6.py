import ansicon

# Nesse ponto o python vai carregar a biblioteca ansicon
ansicon.load()

print("-------------------------------")
print("Aluno 1, Aluno 2, Aluno 3")
print("-------------------------------")

print("")
print("EMPRESA: Aluno 1, Aluno 2, Aluno 3")
print("")

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = float(input("Digite a quantidade: "))

preco_total = preco * quantidade
icms = preco_total * 0.17
ipi = (preco_total - icms) * 0.10

print("\033[1;30;44mProduto\tPreço unitário\tQuantidade\tPreço total\tICMS\033[m")

print("\033[0;35;40m{}\tR$ {:.2f}\t\t\t{}\t\t\tR$ {:.2f}\tR$ {:.2f}\033[m".format(produto, preco, quantidade, preco_total, icms))

input()

# Libera a biblioteca ansicon
ansicon.unload()