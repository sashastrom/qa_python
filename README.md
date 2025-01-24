# qa_python_4

============================================================== test session starts ===============================================================
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0 -- C:\Program Files\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Program Files\Git\qa_python
plugins: cov-6.0.0
collected 12 items                                                                                                                                

tests.py::test_add_new_book PASSED                                                                                                          [  8%] 
tests.py::test_set_book_genre PASSED                                                                                                        [ 16%] 
tests.py::test_get_books_with_specific_genre PASSED                                                                                         [ 25%] 
tests.py::test_get_books_fro_children PASSED                                                                                                [ 33%] 
tests.py::test_add_book_in_favorites PASSED                                                                                                 [ 41%] 
tests.py::test_delete_book_from_favorites PASSED                                                                                            [ 50%] 
tests.py::test_set_multiple_books_genre[Good Detective book-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED [ 58%]
tests.py::test_set_multiple_books_genre[Comedy book-\u041a\u043e\u043c\u0435\u0434\u0438\u0438-\u041a\u043e\u043c\u0435\u0434\u0438\u0438] PASSED [ 66%]
tests.py::test_set_multiple_books_genre[Fantasy book-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 75%]
tests.py::test_books_genre_empty_for_new_books PASSED                                                                                       [ 83%] 
tests.py::test_get_books_with_specific_genre_empty_for_non_existent_genre[Bible-expected0] PASSED                                           [ 91%] 
tests.py::test_get_books_with_specific_genre_empty_for_non_existent_genre[Dr.House-expected1] PASSED                                        [100%] 

=============================================================== 12 passed in 0.46s =============================================================== 