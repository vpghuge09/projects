#service --> what are all options that we are offering to the end user...

from Institute.book_info import Book

class BookService:

    library = []                                #class level --> variable -> class name

    def add_book(self,book_info:Book):          #type(book_info) == Book
        if type(book_info) == Book:
            if book_info.bookId<=0:
                print('Invalid Book Id : ')
            elif book_info.bookPrice<=0:
                print('Invalid Book Price ')
            elif book_info.bookQty<=0:
                print('Invalid Book Qty ')
            elif len(book_info.bookName)<=1 or len(book_info.bookAuthor)<=1:
                print('Invalid Book Name/Author Name')
            else:
                bk = self.search_book(book_info.bookId)                 #search_book -> instance method object ref--
                if bk:
                    print('Duplicate Book Cannot be added')
                else:
                   # BookService.library.append(book_info)
                    file=open('bookinfo.txt','a')
                    bookstr = f'''{book_info.bookId},{book_info.bookName},{book_info.bookPrice},{book_info.bookAuthor},{book_info.bookQty}'''
                    file.writelines(bookstr+"\n")
                    file.close()
                    print('Book Successfully Added')
        else:
            print('Invalid Book Type...')

    def delete_book(self,bkid:int):
        BookService.library = self.get_all_books()  # 5 books
        isBookDeleted = False
        if type(bkid)==int:
            for book in BookService.library:
                if book.bookId == bkid:
                    BookService.library.remove(book)            # 4
                    isBookDeleted = True
                    break
        if isBookDeleted:
            with open("bookinfo.txt", "w") as file:
                 for book_info in BookService.library:
                    bookstr = f'''{book_info.bookId},{book_info.bookName},{book_info.bookPrice},{book_info.bookAuthor},{book_info.bookQty}'''
                    file.writelines(bookstr + "\n")
                    #self.add_book(book)  # fir se write --> updated book bh..
            print(f'Book {bkid} Successfully Deleted')
        else:
            print('Book Id is Invalid So cannot delete')

    def search_book(self,bkid:int):                     #instance method --> object ka ref..self-- object ka ref..
        BookService.library = self.get_all_books()  #
        isElse = False
        if type(bkid) == int and bkid>0:
            for book in BookService.library:
                if book.bookId == bkid:
                   return book
        else:
            print('Invalid Book Id')
            isElse =True

        if not isElse:
            print('Book Not Found')

    def update_book(self, bkid: int, new_book_info: Book):  # reading k liye --> isko value kuch bh
        BookService.library = self.get_all_books()
        if type(bkid)==int and bkid>0:

            #if type(new_book_info) == Book:
            if type(new_book_info)==Book:

                for book in BookService.library:
                    if book.bookId == bkid:
                        new_book_info = new_book_info.__dict__  # book ko convert kiya dict..

                        if new_book_info.get('bookId') and new_book_info.get('bookId') > 0:
                            book.bookId = new_book_info.get('bookId')


                        if new_book_info.get('bookName') and len(new_book_info.get('bookName')) > 1:
                            book.bookName = new_book_info.get('bookName')

                        if new_book_info.get('bookPrice') and new_book_info.get('bookPrice') > 0:
                            book.bookPrice = new_book_info.get('bookPrice')

                        if new_book_info.get('bookQty') and new_book_info.get('bookQty') > 0:
                            book.bookQty = new_book_info.get('bookQty')

                        if new_book_info.get('bookAuthor') and len(new_book_info.get('bookAuthor')) > 1:
                            book.bookAuthor = new_book_info.get('bookAuthor')

                        print('Book Successfully Updated...')
                        with open('bookinfo.txt', 'w') as file:
                            for book_info in BookService.library:
                                bookstr = f'''{book_info.bookId},{book_info.bookName},{book_info.bookPrice},{book_info.bookAuthor},{book_info.bookQty}'''
                                file.writelines(bookstr + "\n")
                        return

            else:
                print("Invalid Book Type")
        else:
            print('Invalid Book Id..:')


    def get_all_books(self):
        with open("bookinfo.txt",'r') as file:
            lines = file.readlines()   # entire file lines
            lines = [line.strip() for line in lines]#strip-- extra \n remove            # i want remove -- prefix - suffix - /n
            booklist = []
            for lin in lines:
                attributes = lin.split(',')     #split -->
                bk = Book(bkid=attributes[0],bknm=attributes[1],bkpric=attributes[2],bkaut=attributes[3],bkqty=attributes[4])
                booklist.append(bk)
            return booklist


    def get_author_specific_books(self,author_name):
        BookService.library = self.get_all_books()
        author_books = []
        for book in BookService.library:
            if book.bookAuthor == author_name:
                author_books.append(book)

        if author_books:
            return author_books
        else:
            print('None of the Book found for this Author...')

    def get_max_price_book(self,max_value=True):
        BookService.library = self.get_all_books()      # reading it from from text
        book_val = None
        if BookService.library:
            if max_value:
                max_price = 0
                for book in BookService.library:
                    if book.bookPrice>max_price:
                        max_price = book.bookPrice
                        book_val = book

                return book_val
        else:
            print('No Book Present So cannot fetch min/max price..')

    def get_min_price_book(self):
        BookService.library = self.get_all_books()
        book_val = None
        if BookService.library:
            min_price = BookService.library[0].bookPrice
            for book in BookService.library:
                if book.bookPrice<min_price:
                    min_price = book.bookPrice
                    book_val = book
            return book_val




