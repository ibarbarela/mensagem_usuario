# ----------------------------------------------------------------             
# PROJETO: Treinamento de Variáveis e Tipos (Nível Estagiário)
# OBJETIVO: Praticar int, float, str, bool e conversão de dados.
# ----------------------------------------------------------------

# EXERCÍCIO 1: Calculadora de Gorjeta (Foco: float e operações)
# Instrução: Receba o valor de uma conta e calcule 10% de gorjeta.
# Lembre-se: O usuário pode digitar com vírgula, trate isso!

valor_da_conta_str = input('Digite o valor da conta: R$')
valor_conta = float(valor_da_conta_str.replace(',','.'))
gorjeta = valor_conta * 0.10
total = valor_conta + gorjeta

print(f"--- Recibo ---")
print(f"Valor original: R$ {valor_conta:.2f}")
print(f"Gorjeta (10%): R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {total:.2f}\n")
