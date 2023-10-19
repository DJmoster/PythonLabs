from MyCSVdb.db import CSVDataBase
from models import Book, User

db1 = CSVDataBase[Book](Book, 'books.csv')
# db1.add(Book('test1', 'Sviat', '20.01.2020', 'Fantasy'))
# db1.add(Book('test2', 'Sviat', '20.01.2020', 'Fantasy'))
# db1.add(Book('test3', 'John', '20.01.2020', 'Horror'))
# db1.add(Book('test3', 'John', '20.01.2020', 'Horror'))
#
# db1.set([Book('test1'), Book('test2')])
#
# db1.update(3, author='Sviat', creation_date='20.05.2021')
# db1.remove(3)
#
# db1.sort(key='creation_date', reverse=False)
#
# data = db1.search(name='test3')
#
# print(db1.unique_count_by('genre'))
#
print(db1.get()[0])

db2 = CSVDataBase[User](User, 'users.csv')
# db2.set([User('Sviat', 18), User('John', 24)])

print(db2.get(0))
