## booklover_test.py - Create BookLover Unit Test Class file

import unittest
    
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        book_lover1 = BookLover('John','jah9kqn@virginia.edu','Non-Fiction')
        
        book_name, book_rating = '1984', 4
        
        book_lover1.add_book(book_name,book_rating)
        
        result = book_name in list(book_lover1.book_list.book_name)
        
        self.assertTrue(result,'Test 1 failed')

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book_lover1 = BookLover('John','jah9kqn@virginia.edu','Non-Fiction')
        
        book_name, book_rating = '1984', 4
        
        try:
            book_lover1.add_book(book_name,book_rating)
        except:
            print('Book is already in list')
        
        try:
            book_lover1.add_book(book_name,book_rating)
        except:
            print('Book is already in list')
        
        expected = 1
        
        result = len([x for x in list(book_lover1.book_list.book_name)])
        
        self.assertEqual(expected, result, 'Test 2 failed')
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book_lover1 = BookLover('John','jah9kqn@virginia.edu','Non-Fiction')
        
        book_name, book_rating = '1984', 4
        
        book_lover1.add_book(book_name,book_rating)
        
        result = book_lover1.has_read(book_name)
        
        self.assertTrue(result, 'Test 3 failed')
        
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book_lover1 = BookLover('John','jah9kqn@virginia.edu','Non-Fiction')
        
        book_name, book_rating = '1984', 4
        
        book_lover1.add_book(book_name,book_rating)
        
        book_name2 = 'The Man'
        
        result = book_lover1.has_read(book_name2)
        
        self.assertFalse(result, 'Test 4 failed')
        
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        book_lover1 = BookLover('John','jah9kqn@virginia.edu','Non-Fiction')
        
        book_name, book_rating = '1984', 4
        book_lover1.add_book(book_name,book_rating)
        
        book_name2, book_rating2 = 'The Man', 4
        book_lover1.add_book(book_name2,book_rating2)
        
        book_name3, book_rating3 = 'Shoe Dog', 3
        book_lover1.add_book(book_name3,book_rating3)
        
        expected = 3
        
        result = book_lover1.num_books_read()
        
        self.assertEqual(expected,result,'Test 5 failed')
        

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        book_lover1 = BookLover('John','jah9kqn@virginia.edu','Non-Fiction')
        
        book_name, book_rating = '1984', 4
        book_lover1.add_book(book_name,book_rating)
        
        book_name2, book_rating2 = 'The Viking Heart', 3 
        book_lover1.add_book(book_name2,book_rating2)
        
        book_name3, book_rating3 = 'The Color of Law', 5
        book_lover1.add_book(book_name3,book_rating3)
        
        fav_book_df = book_lover1.fav_books()
        
        result1 = len(fav_book_df[fav_book_df.book_rating > 3]) >= 1
        result2 = len(fav_book_df[fav_book_df.book_rating <= 3]) == 0
        result = (result1) and (result2)
        
        self.assertTrue(result,'Test 6 failed')
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)