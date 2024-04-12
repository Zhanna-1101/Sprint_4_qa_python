import pytest
from main import BooksCollector


class TestBooksCollector:


    @pytest.mark.parametrize('name', ['Я', 'Цивилизация Статуса', 'Жареные зеленые помидоры кафе Полустанок'])
    def test_add_new_book_add_one_book_with_different_lenght_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(list(collector.books_genre.keys())) == 1
    
    @pytest.mark.parametrize('name', ['', 'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции'])
    def test_add_new_book_not_to_add_book_with_too_long_name_without_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre == {}

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.add_new_book('Убийство в Восточном экспрессе')
        assert len(list(collector.books_genre.keys())) == 2 

    def test_add_new_book_add_books_with_only_original_names(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Сияние')
        assert collector.books_genre == {'Сияние': 'Ужасы'} and len(list(collector.books_genre.keys())) == 1
    
    def test_set_book_genre_add_genre_from_list_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.books_genre['Сияние'] == 'Ужасы'
    
    def test_set_book_genre_not_to_add_genre_not_from_list_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Эпос')
        assert collector.books_genre['Сияние'] == ''
    
    @pytest.mark.parametrize('name, genre', [['Сияние', 'Ужасы'], 
                                             ['Убийство в Восточном экспрессе', 'Детективы'], 
                                             ['Цивилизация Статуса', 'Комедии'], 
                                             ['Дюна', 'Фантастика'], 
                                             ['Русалочка', 'Мультфильмы']])
    def test_get_book_genre_get_right_genre_of_book_by_name_book(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre 
    
    def test_get_books_with_specific_genre_get_list_of_books_with_one_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Доктор Сон')
        collector.set_book_genre('Доктор Сон', 'Ужасы')
        collector.add_new_book('Цивилизация Статуса')
        collector.set_book_genre('Цивилизация Статуса', 'Комедии')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Сияние', 'Доктор Сон']

    def test_get_books_genre_return_current_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_genre() == collector.books_genre
    
    def test_get_books_for_children_get_books_without_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Цивилизация Статуса')
        collector.set_book_genre('Цивилизация Статуса', 'Комедии')
        assert collector.get_books_for_children() == ['Цивилизация Статуса']
    
    def test_add_book_in_favorites_add_book_from_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_book_in_favorites('Сияние')
        assert collector.favorites == ['Сияние']
    
    def test_add_book_in_favorites_not_to_add_book_if_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_book_in_favorites('Сияние')
        collector.add_book_in_favorites('Сияние')
        assert collector.favorites == ['Сияние'] and len(collector.favorites) == 1
    
    def test_add_book_in_favorites_not_to_add_book_if_book_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Сияние')
        assert collector.favorites == []
    
    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_book_in_favorites('Сияние')
        collector.delete_book_from_favorites('Сияние')
        assert collector.favorites == [] and len(collector.favorites) == 0
    
    def test_get_list_of_favorites_books_get_whole_list_books_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Цивилизация Статуса')
        collector.set_book_genre('Цивилизация Статуса', 'Комедии')
        collector.add_book_in_favorites('Сияние')
        collector.add_book_in_favorites('Цивилизация Статуса')
        assert collector.get_list_of_favorites_books() == ['Сияние', 'Цивилизация Статуса'] and collector.favorites == ['Сияние', 'Цивилизация Статуса'] 
