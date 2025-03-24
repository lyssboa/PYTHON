idade = int(input("Qual a sua idade? "))
if idade > 16: 
    print("Não precisa votar!");
elif idade == 16 or idade > 65:
    print("Voto não obrigatório");
else:
    print("Voto obrigatório");
