import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

def test_add_new_book(collector):
    collector.add_new_book("Harry Potter")
    assert "Harry Potter" in collector.get_books_genre()

def test_set_book_genre(collector):
    collector.add_new_book("2025")
    collector.set_book_genre("2025", "Детективы")
    assert collector.get_book_genre("2025") == "Детективы"
    collector.set_book_genre('no name',"Ужасы")
    assert collector.get_book_genre('no name') is None

def test_get_books_with_specific_genre(collector):
    collector.add_new_book("Master&Margarita")
    collector.set_book_genre("Master&Margarita", "Фантастика")
    collector.add_new_book("Mister Bin")
    collector.set_book_genre("Mister Bin", "Комедии")
    books = collector.get_books_with_specific_genre("Фантастика")
    assert "Master&Margarita" in books
    assert "Mister Bin" not in books

def test_get_books_fro_children(collector):
    collector.add_new_book("Tom&Jerry")
    collector.set_book_genre("Tom&Jerry", "Мультфильмы")
    collector.add_new_book("Dracula")
    collector.set_book_genre("Dracula","Ужасы")
    books_for_child = collector.get_books_for_children()
    assert "Tom&Jerry" in books_for_child
    assert "Dracula" not in books_for_child


def test_add_book_in_favorites():
    collector = BooksCollector()
    collector.add_new_book("Fantasy")
    collector.set_book_genre("Fantasy", "Фантастика")
    collector.add_book_in_favorites("Fantasy")
    assert "Fantasy" in collector.get_list_of_favorites_books()


def test_delete_book_from_favorites(collector):
    collector.add_new_book("Peter Pen")
    collector.set_book_genre("Peter Pen", "Мультфильмы")
    collector.add_book_in_favorites("Peter Pen")
    collector.delete_book_from_favorites("Peter Pen")
    assert "Peter Pen" not in collector.get_list_of_favorites_books()
    collector.delete_book_from_favorites("no name")
    assert len(collector.get_list_of_favorites_books()) == 0

@pytest.mark.parametrize("book_name, genre, expected", [
    ("Good Detective book", "Детективы", "Детективы"),
    ("Comedy book", "Комедии", "Комедии"),
    ("Fantasy book", "Фантастика", "Фантастика"),
])

def test_set_multiple_books_genre(collector, book_name, genre, expected):
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == expected

def test_books_genre_empty_for_new_books(collector):
    collector.add_new_book("new Book 2025")
    assert collector.get_book_genre("new Book 2025") == ""


@pytest.mark.parametrize("book_name, expected", [
    ("Bible", []),
    ("Dr.House", []),
])
def test_get_books_with_specific_genre_empty_for_non_existent_genre(book_name, expected):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, "Детективы")
    books = collector.get_books_with_specific_genre("Фантастика")
    assert books == expected
