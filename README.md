## Biblioteki

- Komm
- Pandas
- NumPy
- matplotlib.pyplot
- SciPy (scipy.signal)
- Pillow / OpenCV

## Założenia

- Porównanie algorytmów korekcyjnych, wpływ kanałów (FEC, potrajanie bitów, BCH, CRC, Hamming)
- Algorytm programu ma być generyczny, nie ważne na jakich danych operuje (tekst / obraz)

## Proces testów

- Przygotowanie danych testowych (tekst / obraz)
- Zakodowanie w Komm
- Przetworzenie kanałem w Komm
- Dekodowanie w Komm
- Interpretacja stosownie do danych wejściowych


## Run Locally

Clone the project

```bash
  git clone https://github.com/SentiWW/niduc.git
```

Install requirement packages

```bash
  pip install -r requirements.txt
```

Run the code

```bash
  python main.py
```