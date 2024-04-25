from datetime import datetime

#Define o array que vai receber os horarios de entrada e saida
listaHorarios = []

while True:
    #Solicitando ao usuario os dois horarios
    horarioCompleto = input("Digite os horarios de Entrada e Saida (no formato HH:MM - HH:MM) ou digite 'sair' para encerrar: ")

    #Verifica se o usuario deseja sair
    if horarioCompleto.lower() == "sair":
        break

    #dando um split nos horarios
    horarioEntrada, horarioSaida = horarioCompleto.split(" - ")

    #atribuindo os dois horarios a um par ordenado
    conjuntoHorarios = (horarioEntrada, horarioSaida)

    #Colocando o par ordenado dentro do array
    listaHorarios.append(conjuntoHorarios)

    def diferencaEntreHorarios(entradaHorario, saidaHorario):
        entrada_obj = datetime.strptime(entradaHorario, "%H:%M")
        saida_obj = datetime.strptime(saidaHorario, "%H:%M")
        diferenca = saida_obj - entrada_obj

        horasTrabalhadas = diferenca.total_seconds() / 3600  # Convertendo diferença para minutos
        return horasTrabalhadas

#Exibe a lista de horarios
print("Lista de horarios:")
for i, (entrada, saida) in enumerate(listaHorarios, start=1) :
    print(f"Dia {i}: Entrada: {entrada}, Saida: {saida}, Horas Trabalhadas: {diferencaEntreHorarios(entrada, saida)}")

# Calcula o total de horas trabalhadas
total_horas_trabalhadas = sum(diferencaEntreHorarios(entrada, saida) for entrada, saida in listaHorarios)
print(f"\nTotal de horas trabalhadas: {total_horas_trabalhadas:.2f} horas")