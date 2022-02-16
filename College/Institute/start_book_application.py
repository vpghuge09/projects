

from Institute.book_info import Book
from Institute.book_service import BookService

service = BookService()

def get_input_from_user():
    bid = int(input('Enter Book Id : '))
    bnm = input('Enter Book Name : ')
    baut = input('Enter Book Author : ')
    bprc = float(input('Enter Book Price : '))
    bqty = int(input('Enter Book Qty : '))
    #return Book(bid,bnm,baut,bprc,bqty)                                    #positional
    return Book(bkid=bid,bknm=bnm,bkaut=baut,bkpric=bprc,bkqty=bqty)        #named param

def add_book_input():
    book = get_input_from_user()
    service.add_book(book)


def delete_book_input():
    bkid = int(input('Enter Book Id for Delete : '))
    service.delete_book(bkid)

def update_book_input():
    service.get_all_books()
    ch = int(input("enter book id...:"))
    book=get_input_from_user()
    service.update_book(ch,book)



def get_allbook_info():
    book=service.get_all_books()
    print(book)

def search_by_id():
    bid = int(input("Enter book id...:"))
    book = service.search_book(bid)
    print(book)



def get_max_price():
    pr=service.get_max_price_book()
    print(pr)

def get_min_price():
    pr=service.get_min_price_book()
    print(pr)

def search_by_author():
    auth=input("Enter author name")
    book=service.get_author_specific_books(auth)
    print(book)



if __name__=='__main__':
    while True:
        print('''Enter your choice :
        1.Add book
        2.Remove book
        3.Search book
        4.Show all book
        5.Search by author
        6.Max price of book
        7.Min price of book
        8.update_Book
         ''')
        choice = int(input("Enter your choice...:"))
        if choice == 1:
            add_book_input()
        elif choice == 2:
            delete_book_input()
        elif choice == 3:
            search_by_id()

        elif choice == 4:
            get_allbook_info()
        elif choice == 5:
            search_by_author()
        elif choice == 6:
            get_max_price()


        elif choice == 7:
            get_min_price()

        elif choice == 8:
            update_book_input()

        else:
            print ("invalid choice")

#get_input_from_user()
#add_book_input()
#delete_book_input()
#get_allbook_info()
#get_max_min_price()
#search_by_author()