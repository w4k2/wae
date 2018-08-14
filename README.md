# WAE

Eksperymenty powinny dotyczyć dwóch elementów:

- wpływu parametrów na jakość klasyfikatora
- porównania klasyfikatora z innymi metodami klasyfikacji streamów

Do eksperymentów należy użyc dość sporej liczby baz. Zarówno syntetycznych, ale także innych znanych z literatury. Należy określić jakość algorytmów z wykorzystaniem metody *test and train*:

1. average accuracy
2. standard deviation
3. accuracy dla każdego chunka (wykres)
4. average processing (zarówno testing, jak i training) time
5. standard deviation of processing time (zarówno testing, jak i training) 6. average memory usage
7. standard deviation of memory usage
8. memory usage dla każdego chunka

> Proszę zapisz dane abyśmy mogli później je użyć do analizy statystycznej!!!

## Eksperyment 1 — wpływ parametrów na jakość klasyfikatora WAE

- porównanie dla różnych metod kalkulacji wag (tutaj także należy porów- nać dla różnych wartosci parametru /teta)
- porównanie dla różnych metod postarzania(tutaj także należy porównać dla różnych wartosci parametru /teta)
- pokazać dla kilku metod, czy odmładzania daje poztywny efekt
- eksperymenty należy preprowadzić dla puli homogenicznej (dla kilku kla- syfikatorów bazowych, tzn. sieci neuronowe, drzewa decyzyjne, k-nn) oraz dla puli klasyfikatorów heterogenicznych

## Eksperyment 2 - porównanie WAE z innymi klasyfikatorami

Porównanie kilku najlepszych ustawień z eksperymentu 1 z klasyfikatorami zna- nymi z literatury.
