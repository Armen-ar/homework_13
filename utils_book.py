import json


def load_books_from_json():
    """
    Загружает книжки из файла
    """
    with open("books.json", "r", encoding="utf-8") as file:
        books = json.load(file)
    return books


def save_books_to_json(books: dict) -> None:
    """
    Сохраняет список словарей в json файл
    """

    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False)


def get_books() -> list[dict]:
    """
    Получает все книги
    """
    books = load_books_from_json()
    return books


def get_book_by_id(book_id: int):
    """
    Получает одну книгу по id
    """
    books = load_books_from_json()
    for book in books:
        if book["id"] == book_id:
            return book


def add_book(book_data: dict) -> dict:
    """
    Записывает новую книгу в файл
    Словарь с данными книги
    """

    books = load_books_from_json()
    last_book = books[-1]
    last_id = last_book["id"]
    book_data["id"] = last_id + 1

    books.append(book_data)
    save_books_to_json(books)
    return book_data


def update_book(book_id: int, book_data: str):
    """
    Обновляет книгу с нужным id
    """

    books = load_books_from_json()
    for book in books:
        if book["id"] == book_id:
            books = book_data
            break
    save_books_to_json(books)


def delete_book(book_id: int):
    """
    Удаляет книгу с указанным book_id
    """

    books = load_books_from_json()
    for index, book in enumerate(books):
        if book["id"] == book_id:
            del books[index]
            break
    save_books_to_json(books)
