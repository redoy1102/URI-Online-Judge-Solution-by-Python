N1, N2, N3, N4 = [float(x) for x in input().split()]

avr = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10
print("Media:", round(avr, 1))

if avr >= 7.0:
    print("Aluno aprovado.")
elif avr < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= avr <= 6.9:
    print("Aluno em exame.")
    n5 = input()
    N5 = float(n5)
    print("Nota do exame:", N5)

    avr2 = (avr + N5) / 2
    if avr2 >= 5.0:
        print("Aluno aprovado.")
        print("Media final:", avr2)
    elif avr2 <= 4.9:
        print("Aluno reprovado.")
        print("Media final:", avr2)