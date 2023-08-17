import utils
import ms
import bs
import quicksort
import qs

bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')


def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']


def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] < book_b['author_lower']


def by_total_length(book_a, book_b):
    return len(book_a['author']) + len(book_a['title']) > len(book_b['author']) + len(book_b['author'])


# for book in bookshelf:
#     print(book['title'])

# sort1 = bs.bubble_sort(bookshelf, by_title_ascending)
# print(sort1)

# bookshelf_v1 = bookshelf
# bookshelf_v2 = bookshelf

# sort2 = bs.bubble_sort(bookshelf_v1, by_author_ascending)
# print(sort2)

# quicksort.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
# print(bookshelf_v2)

# sort_long = bs.bubble_sort(long_bookshelf, by_total_length)
sort_long = quicksort.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
print(sort_long)