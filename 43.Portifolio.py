def calcula_imc(peso, altura):

    # Calcula o IMC 
    imc = peso / (altura ** 2)
    return imc

def classifica_imc(imc_calculado):

    # Classifica o IMC 
    if imc_calculado < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc_calculado < 24.9:
        return "Peso normal"
    elif 25 <= imc_calculado < 29.9:
        return "Sobrepeso"
    elif 30 <= imc_calculado < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc_calculado < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def main():

        peso_pessoa = float(input("Digite quantos quilos você pesa: "))
        altura_pessoa = float(input("Digite sua altura em metros: "))
        
        imc_pessoa = calcula_imc(peso_pessoa, altura_pessoa)
        
        print(f"Seu IMC é: {imc_pessoa}")
        
        # Classifica o IMC e exibe o resultado
        classificacao_imc = classifica_imc(imc_pessoa)
        print(f"Classificação: {classificacao_imc}")

if __name__ == "__main__":
    main()