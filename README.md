# Monitor wydatków domowych

## Spis treści

1. Opis projektu
2. Funkcjonalności
3. Technologie
4. Struktura projektu
5. Instrukcja uruchomienia
6. Testy
7. Autor

## Opis projektu

Monitor wydatków domowych to aplikacja internetowa wykonana w technologii Django.  
Projekt realizuje wzorzec architektoniczny MVC w postaci stosowanej przez Django, czyli MTV:

- Model odpowiada za strukturę danych,
- View obsługuje logikę żądań HTTP,
- Template odpowiada za warstwę prezentacji.

Aplikacja pozwala zarządzać domowymi wydatkami poprzez dodawanie, edycję, usuwanie i filtrowanie pozycji.  
Projekt został przygotowany jako zadanie nr 13: System monitorowania wydatków domowych.


## Funkcjonalności

Aplikacja umożliwia:

- wyświetlanie listy wydatków,
- dodawanie nowych wydatków,
- edycję istniejących wydatków,
- usuwanie wydatków,
- przypisywanie wydatków do kategorii,
- filtrowanie wydatków po kategorii,
- filtrowanie wydatków po zakresie dat,
- obliczanie łącznej sumy wydatków,
- wyświetlanie wykresu wydatków według kategorii,
- zarządzanie danymi z poziomu panelu administratora Django.

## Technologie

W projekcie wykorzystano:

- Python,
- Django,
- SQLite,
- HTML,
- Bootstrap,
- Chart.js.

## Struktura projektu

```text
expense_tracker/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── expenses/
│   ├── templates/
│   │   └── expenses/
│   │       ├── base.html
│   │       ├── expense_list.html
│   │       ├── expense_form.html
│   │       └── expense_confirm_delete.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── README.md

## Przykładowe dane

W folderze `sample_data` znajduje się plik `expenses_sample.json`, który zawiera przykładowe dane wejściowe dla aplikacji.