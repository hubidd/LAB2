import matplotlib.pyplot as plt

dane = input("Podaj liczby całkowite oddzielone spacją: ")
if not dane.strip():
    print("Nie wprowadzono żadnych danych.")
else:
    liczby = [int(x) for x in dane.split()]
    suma = sum(liczby)
    srednia = suma / len(liczby)
    dodatnie = len([x for x in liczby if x > 0])
    ujemne = len([x for x in liczby if x < 0])
    zera = len([x for x in liczby if x == 0])

    print("Wyniki:")
    print("Liczb razem:", len(liczby))
    print("Suma:", suma)
    print("Średnia:", round(srednia, 2))
    print("Dodatnie:", dodatnie)
    print("Ujemne:", ujemne)
    print("Zera:", zera)
    print("Maksimum:", max(liczby))
    print("Minimum:", min(liczby))

    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.hist(liczby, bins=10, edgecolor='black')
    plt.title("Histogram")
    plt.subplot(1, 3, 2)
    plt.bar(["Dodatnie", "Ujemne", "Zera"], [dodatnie, ujemne, zera],
            color=["green", "red", "gray"])

    plt.title("Porównanie")
    plt.subplot(1, 3, 3)
    plt.plot(liczby, marker='o')
    plt.title("Kolejność liczb")

    plt.tight_layout()
    plt.show()
