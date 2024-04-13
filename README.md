# qa_python - 4 sprint

### Тесты для метода add_new_book:
- __test_add_new_book_add_one_book_with_different_lenght_name__ - параметризованный тест. Проверяется добавление в словарь books_genre книг с разной длиной наименования: 1 символ, 19 символов, 40 символов - в пределах разрешенного диапазона длины наименования.

- __test_add_new_book_not_to_add_book_with_too_long_name_without_name__ - параметризованный тест. Проверяется недобавление в словарь books_genre книг длина наименования которых: 0 символов, более 40 символов - за пределами разрешенного диапазона длины наименования.

- __test_add_new_book_add_two_books__ - проверяется добавление в словарь двух книг подряд.
        
- __test_add_new_book_add_books_with_only_original_names__ - проверяется невозможность добавления в словарь двух книг с одинаковым наименованием.
        
### Тесты для метода set_book_genre:
- __test_set_book_genre_add_genre_from_list_genre__ - проверяется добавление книге жанра, присутствующего в списке жанров genre. 
    
- __test_set_book_genre_not_to_add_genre_not_from_list_genre__ - проверяется невозможность добавления книге жанра, отсутствующего в списке жанров genre.
       
### Тесты для метода get_book_genre:
- __test_get_book_genre_get_right_genre_of_book_by_name_book__ - параметризованный тест. Проверяется соответствие выводимого жанра книги - установленному жанру книги.
       
### Тесты для метода get_books_with_specific_genre:
- __test_get_books_with_specific_genre_get_list_of_books_with_one_genre__ - проверяется правильность вывода списка книг имеющих один и тот же жанр.
        
### Тесты для метода get_books_genre:
- __test_get_books_genre_return_current_books_genre__ - проверяется соответствие вывода из словаря books_genre, получаемого методом get_books_genre - содержанию словаря books_genre.
        
### Тесты для метода get_books_for_children:
- __test_get_books_for_children_get_books_without_rating__ - проверяется, что метод не выводит в список книг для детей, книги с жанром, присутствующим в списке genre_age_rating.
        
### Тесты для метода add_book_in_favorites:
- __test_add_book_in_favorites_add_book_from_books_genre__ - проверяется добавление книги, находящейся в словаре books_genre, в список favorites.
    
- __test_add_book_in_favorites_not_to_add_book_if_book_in_favorites__ - проверяется невозможность повторного добавления книги, уже находящейся в списке favorites - в этот список.
    
- __test_add_book_in_favorites_not_to_add_book_if_book_not_in_books_genre__ - проверяется невозможность добавления в список favorites, книги, отсутствующей в books_genre.
 
### Тесты для метода delete_book_from_favorites:
- __test_delete_book_from_favorites_delete_one_book__ - проверяется удаление книги, ранее добавленной в список favorites.
        
### Тесты для метода get_list_of_favorites_books:
- __test_get_list_of_favorites_books_get_whole_list_books_from_favorites__ - проверяется соответствие списка, полученонго мтетодом get_list_of_favorites_books - списку favorites.
