from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



books = [
    { 'id': 1,
        'title': 'Introduction to the Theory of Computation',
        'author': 'Michael Sipser ',
        'description': 'Covers the fundamentals of computation theory.',
        'image': 'library.jpeg',
        'link': 'Introduction-To-The-Theory-Of-Computation-Michael-Sipser.pdf' },
    {'id': 2, 'title': 'Clean Code', 'author': 'Robert C. Martin', 'description': 'A Handbook of Agile Software Craftsmanship.', 'image': 'https://spin.atomicobject.com/wp-content/uploads/Clean-Code.jpg','link': 'https://www.scribd.com/document/768715748/Clean-Code' },
    {'id': 3, 'title': 'The Pragmatic Programmer', 'author': 'Andrew Hunt and David Thomas', 'description': 'Tips and techniques for software development.', 'image': 'https://i.pinimg.com/736x/81/21/dc/8121dc48ec937ecf919bc2c54aa961a4.jpg', 'link': 'https://www.google.com.ng/books/edition/The_Pragmatic_Programmer/5wBQEp6ruIAC?hl=en&gbpv=0'},
    {'id': 4, 
     'title': 'Design Patterns: Elements of Reusable Object-Oriented Software', 'author': 'Erich Gamma et al.', 'description': 'A guide to software design patterns.', 'image': 'https://i.pinimg.com/736x/82/bf/dc/82bfdc2debbb46293e2c2444c4311c05.jpg','link':'chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/http://www.uml.org.cn/c++/pdf/DesignPatterns.pdf'},
    {'id': 5, 'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell and Peter Norvig', 'description': 'Comprehensive introduction to AI.', 'image': 'https://placekitten.com/200/304'},
    {'id': 6, 'title': 'The Art of Computer Programming', 'author': 'Donald E. Knuth', 'description': 'A comprehensive monograph on algorithms.', 'image': 'https://placekitten.com/200/305'},
    {'id': 7, 'title': 'Code Complete', 'author': 'Steve McConnell', 'description': 'A practical guide to software construction.', 'image': 'https://placekitten.com/200/306'},
    {'id': 8, 'title': 'Introduction to Algorithms', 'author': 'Thomas H. Cormen et al.', 'description': 'Comprehensive textbook on algorithms.', 'image': 'https://placekitten.com/200/307'},
    {'id': 9, 'title': 'Computer Networking: A Top-Down Approach', 'author': 'James Kurose and Keith Ross', 'description': 'Introduction to computer networking.', 'image': 'https://placekitten.com/200/308'},
    {'id': 10, 'title': 'The Mythical Man-Month', 'author': 'Frederick P. Brooks Jr.', 'description': 'Reflections on software engineering management.', 'image': 'https://placekitten.com/200/309'},
    {'id': 11, 'title': 'You Don\'t Know JS', 'author': 'Kyle Simpson', 'description': 'A series on JavaScript programming.', 'image': 'https://placekitten.com/200/310'},
    {'id': 12, 'title': 'Deep Learning', 'author': 'Ian Goodfellow et al.', 'description': 'Comprehensive guide to deep learning.', 'image': 'https://placekitten.com/200/311'},
    {'id': 13, 'title': 'Computer Vision: Algorithms and Applications', 'author': 'Richard Szeliski', 'description': 'A comprehensive guide to computer vision.', 'image': 'https://placekitten.com/200/312'},
    {'id': 14, 'title': 'The Clean Coder', 'author': 'Robert C. Martin', 'description': 'A code of conduct for professional programmers.', 'image': 'https://placekitten.com/200/313'},
    {'id': 15, 'title': 'Introduction to Machine Learning', 'author': 'Ethem Alpaydin', 'description': 'An overview of machine learning concepts.', 'image': 'https://placekitten.com/200/314'},
    {'id': 16, 'title': 'Artificial Intelligence for Humans', 'author': 'Jeff Heaton', 'description': 'An introduction to AI concepts.', 'image': 'https://placekitten.com/200/315'},
    {'id': 17, 'title': 'Computer Architecture: A Quantitative Approach', 'author': 'John L. Hennessy and David A. Patterson', 'description': 'In-depth study of computer architecture.', 'image': 'https://placekitten.com/200/316'},
    {'id': 18, 'title': 'The Algorithm Design Manual', 'author' : 'Jeffrey S. Vitter', 'description': 'A comprehensive guide to algorithm design.', 'image': 'https://placekitten.com/200/317'},

    {'id': 19, 'title': 'Elements of Programming Interviews', 'author': 'Adnan Aziz et al.', 'description': 'A guide to programming interview questions.', 'image': 'https://placekitten.com/200/318'},

    {'id': 20, 'title': 'Introduction to the Theory of Computation', 'author': 'Michael Sipser', 'description': 'Fundamentals of computation theory.', 'image': 'https://placekitten.com/200/319'},

    {'id': 21, 'title': 'Artificial Intelligence: Foundations of Computational Agents', 'author': 'David L. Poole and Alan K. Mackworth', 'description': 'A comprehensive introduction to AI.', 'image': 'https://placekitten.com/200/320'},

    {'id': 22, 'title': 'Computer Graphics: Principles and Practice', 'author': 'John F. Hughes et al.', 'description': 'A foundational text on computer graphics.', 'image': 'https://placekitten.com/200/321'},

    {'id': 23, 'title': 'Operating System Concepts', 'author': 'Abraham Silberschatz et al.', 'description': 'A comprehensive guide to operating systems.', 'image': 'https://placekitten.com/200/322'},

    {'id': 24, 'title': 'Database System Concepts', 'author': 'Abraham Silberschatz et al.', 'description': 'An introduction to database systems.', 'image': 'https://placekitten.com/200/323'},

    {'id': 25, 'title': 'Computer Networks', 'author': 'Andrew S. Tanenbaum', 'description': 'A comprehensive introduction to networking.', 'image': 'https://placekitten.com/200/324'},

    {'id': 26, 'title': 'Introduction to the Theory of Computation', 'author': 'Michael Sipser', 'description': 'Fundamentals of computation theory.', 'image': 'https://placekitten.com/200/325'},

    {'id': 27, 'title': 'Software Engineering at Google', 'author': 'Titania McGrath et al.', 'description': 'Insights into software engineering practices at Google.', 'image': 'https://placekitten.com/200/326'},

    {'id': 28, 'title': 'The Art of Electronics', 'author': 'Paul Horowitz and Winfield Hill', 'description': 'A comprehensive guide to electronics.', 'image': 'https://placekitten.com/200/327'},

    {'id': 29, 'title': 'Introduction to Quantum Computing', 'author': 'Michael A. Nielsen and Isaac L. Chuang', 'description': 'An introduction to quantum computing concepts.', 'image': 'https://placekitten.com/200/328'},

    {'id': 30, 'title': 'Computer Security: Principles and Practice', 'author': 'William Stallings and Lawrie Brown', 'description': 'A comprehensive guide to computer security.', 'image': 'https://placekitten.com/200/329'},

    {'id': 31, 'title': 'The Design of the UNIX Operating System', 'author': 'Maurice J. Bach', 'description': 'A detailed look at UNIX system design.', 'image': 'https://placekitten.com/200/330'},

    {'id': 32, 'title': 'Compilers: Principles, Techniques, and Tools', 'author': 'Alfred V. Aho et al.', 'description': 'A foundational text on compiler design.', 'image': 'https://placekitten.com/200/331'},

    {'id': 33, 'title': 'Introduction to Information Retrieval', 'author': 'Christopher D. Manning et al.', 'description': 'A comprehensive guide to information retrieval.', 'image': 'https://placekitten.com/200/332'},

    {'id': 34, 'title': 'Computer Vision: A Modern Approach', 'author': 'David Forsyth and Jean Ponce', 'description': 'A comprehensive guide to computer vision.', 'image': 'https://placekitten.com/200/333'},

    {'id': 35, 'title': 'Machine Learning: A Probabilistic Perspective', 'author': 'Kevin P. Murphy', 'description': 'An introduction to probabilistic machine learning.', 'image': 'https://placekitten.com/200/334'},

   
    {'id': 36, 'title': 'Data Mining: Concepts and Techniques', 'author': 'Jiawei Han et al.', 'description': 'A comprehensive guide to data mining techniques.', 'image': 'https://placekitten.com/200/335'},

    {'id': 37, 'title': 'Introduction to the Theory of Computation', 'author': 'Michael Sipser', 'description': 'Fundamentals of computation theory.', 'image': 'https://placekitten.com/200/336'},

    {'id': 38, 'title': 'The Elements of Statistical Learning', 'author': 'Trevor Hastie et al.', 'description': 'A comprehensive guide to statistical learning.', 'image': 'https://placekitten.com/200/337'},

    {'id': 39, 'title': 'Artificial Intelligence: A Guide to Intelligent Systems', 'author': 'Michael Negnevitsky', 'description': 'An introduction to intelligent systems.', 'image': 'https://placekitten.com/200/338'},

    {'id': 40, 'title': 'Introduction to Machine Learning', 'author': 'Ethem Alpaydin', 'description': 'An overview of machine learning concepts.', 'image': 'https://placekitten.com/200/339'},

    {'id': 41, 'title': 'Computer Graphics: Principles and Practice', 'author': 'John F. Hughes et al.', 'description': 'A foundational text on computer graphics.', 'image': 'https://placekitten.com/200/340'},

    {'id': 42, 'title': 'Digital Design and Computer Architecture', 'author': 'David Harris and Sarah Harris', 'description': 'A comprehensive guide to digital design.', 'image': 'https://placekitten.com/200/341'},

    {'id': 43, 'title': 'Introduction to the Theory of Computation', 'author': 'Michael Sipser', 'description': 'Fundamentals of computation theory.', 'image': 'https://placekitten.com/200/342'},

    {'id': 44, 'title': 'Computer Vision: Algorithms and Applications', 'author': 'Richard Szeliski', 'description': 'A comprehensive guide to computer vision.', 'image': 'https://placekitten.com/200/343'},

    {'id': 45, 'title': 'The Art of Computer Programming', 'author': 'Donald E. Knuth', 'description': 'A comprehensive monograph on algorithms.', 'image': 'https://placekitten.com/200/344'},

    {'id': 46, 'title': 'Introduction to Quantum Computing', 'author': 'Michael A. Nielsen and Isaac L. Chuang', 'description': 'An introduction to quantum computing concepts.', 'image': 'https://placekitten.com/200/345'},

    {'id': 47, 'title': 'Computer Networking: A Top-Down Approach', 'author': 'James Kurose and Keith Ross', 'description': 'Introduction to computer networking.', 'image': 'https://placekitten.com/200/346'},

    {'id': 48, 'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell and Peter Norvig', 'description': 'Comprehensive introduction to AI.', 'image': 'https://placekitten.com/200/347'},

    {'id': 49, 'title': 'The Clean Coder', 'author': 'Robert C. Martin', 'description': 'A code of conduct for professional programmers.', 'image': 'https://placekitten.com/200/348'},

    {'id': 50, 'title': 'Compilers: Principles, Techniques, and Tools', 'author': 'Alfred V. Aho et al.', 'description': 'A foundational text on compiler design.', 'image': 'https://placekitten.com/200/349'},

    {'id': 51, 'title': 'Computer Architecture: A Quantitative Approach', 'author': 'John L. Hennessy and David A. Patterson', 'description': 'In-depth study of computer architecture.', 'image': 'https://placekitten.com/200/350'},

    {'id': 52, 'title': 'Machine Learning: A Probabilistic Perspective', 'author': 'Kevin P. Murphy', 'description': 'An introduction to probabilistic machine learning.', 'image': 'https://placekitten.com/200/351'},

    {'id': 53, 'title': 'Data Mining: Concepts and Techniques', 'author': 'Jiawei Han et al.', 'description': 'A comprehensive guide to data mining techniques.', 'image': 'https ://placekitten.com/200/352'},

    {'id': 54, 'title': 'Introduction to Information Retrieval', 'author': 'Christopher D. Manning et al.', 'description': 'A comprehensive guide to information retrieval.', 'image': 'https://placekitten.com/200/353'},

    {'id': 55, 'title': 'Computer Security: Principles and Practice', 'author': 'William Stallings and Lawrie Brown', 'description': 'A comprehensive guide to computer security.', 'image': 'https://placekitten.com/200/354'},

    {'id': 56, 'title': 'Digital Design and Computer Architecture', 'author': 'David Harris and Sarah Harris', 'description': 'A comprehensive guide to digital design.', 'image': 'https://placekitten.com/200/355'},

    {'id': 57, 'title': 'The Algorithm Design Manual', 'author': 'Steven S. Skiena', 'description': 'A comprehensive guide to algorithm design.', 'image': 'https://placekitten.com/200/356'},

    {'id': 58, 'title': 'Introduction to Machine Learning', 'author': 'Ethem Alpaydin', 'description': 'An overview of machine learning concepts.', 'image': 'https://placekitten.com/200/357'},

    {'id': 59, 'title': 'Computer Graphics: Principles and Practice', 'author': 'John F. Hughes et al.', 'description': 'A foundational text on computer graphics.', 'image': 'https://placekitten.com/200/358'},

    {'id': 60, 'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell and Peter Norvig', 'description': 'Comprehensive introduction to AI.', 'image': 'https://placekitten.com/200/359'},

    {'id': 61, 'title': 'The Clean Coder', 'author': 'Robert C. Martin', 'description': 'A code of conduct for professional programmers.', 'image': 'https://placekitten.com/200/360'},

    {'id': 62, 'title': 'Compilers: Principles, Techniques, and Tools', 'author': 'Alfred V. Aho et al.', 'description': 'A foundational text on compiler design.', 'image': 'https://placekitten.com/200/361'},

    {'id': 63, 'title': 'Computer Architecture: A Quantitative Approach', 'author': 'John L. Hennessy and David A. Patterson', 'description': 'In-depth study of computer architecture.', 'image': 'https://placekitten.com/200/362'},

    {'id': 64, 'title': 'Machine Learning: A Probabilistic Perspective', 'author': 'Kevin P. Murphy', 'description': 'An introduction to probabilistic machine learning.', 'image': 'https://placekitten.com/200/363'},

    {'id': 65, 'title': 'Data Mining: Concepts and Techniques', 'author': 'Jiawei Han et al.', 'description': 'A comprehensive guide to data mining techniques.', 'image': 'https://placekitten.com/200/364'},

    {'id': 66, 'title': 'Introduction to Information Retrieval', 'author': 'Christopher D. Manning et al.', 'description': 'A comprehensive guide to information retrieval.', 'image': 'https://placekitten.com/200/365'},

    {'id': 67, 'title': 'Computer Security: Principles and Practice', 'author': 'William Stallings and Lawrie Brown', 'description': 'A comprehensive guide to computer security.', 'image': 'https://placekitten.com/200/366'},

    {'id': 68, 'title': 'Digital Design and Computer Architecture', 'author': 'David Harris and Sarah Harris', 'description': 'A comprehensive guide to digital design.', 'image': 'https://placekitten.com/200/367'},

    {'id': 69, 'title': 'The Algorithm Design Manual', 'author': 'Steven S. Skiena', 'description': 'A comprehensive guide to algorithm design.', 'image': 'https://placekitten.com/200/368'},

    {'id': 70, 'title': 'Introduction to Machine Learning', 'author': 'Ethem Alpaydin', 'description': 'An overview of machine learning concepts.', 'image': 'https://placekitten.com/200/369'},

    {'id': 71, 'title': 'Computer Graphics: Principles and Practice', 'author': 'John F. Hughes et al.', 'description': 'A foundational text on computer graphics.', 'image': 'https ```python'},
    {'id': 71, 'title': 'Computer Graphics: Principles and Practice', 'author': 'John F. Hughes et al.', 'description': 'A foundational text on computer graphics.', 'image': 'https://placekitten.com/200/370'},

    {'id': 72, 'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell and Peter Norvig', 'description': 'Comprehensive introduction to AI.', 'image': 'https://placekitten.com/200/371'},

    {'id': 73, 'title': 'The Clean Coder', 'author': 'Robert C. Martin', 'description': 'A code of conduct for professional programmers.', 'image': 'https://placekitten.com/200/372'},

    {'id': 74, 'title': 'Compilers: Principles, Techniques, and Tools', 'author': 'Alfred V. Aho et al.', 'description': 'A foundational text on compiler design.', 'image': 'https://placekitten.com/200/373'},

    {'id': 75, 'title': 'Computer Architecture: A Quantitative Approach', 'author': 'John L. Hennessy and David A. Patterson', 'description': 'In-depth study of computer architecture.', 'image': 'https://placekitten.com/200/374'},

    {'id': 76, 'title': 'Machine Learning: A Probabilistic Perspective', 'author': 'Kevin P. Murphy', 'description': 'An introduction to probabilistic machine learning.', 'image': 'https://placekitten.com/200/375'},

    {'id': 77, 'title': 'Data Mining: Concepts and Techniques', 'author': 'Jiawei Han et al.', 'description': 'A comprehensive guide to data mining techniques.', 'image': 'https://placekitten.com/200/376'},

    {'id': 78, 'title': 'Introduction to Information Retrieval', 'author': 'Christopher D. Manning et al.', 'description': 'A comprehensive guide to information retrieval.', 'image': 'https://placekitten.com/200/377'},

    {'id': 79, 'title': 'Computer Security: Principles and Practice', 'author': 'William Stallings and Lawrie Brown', 'description': 'A comprehensive guide to computer security.', 'image': 'https://placekitten.com/200/378'},

    {'id': 80, 'title': 'Digital Design and Computer Architecture', 'author': 'David Harris and Sarah Harris', 'description': 'A comprehensive guide to digital design.', 'image': 'https://placekitten.com/200/379'},

    {'id': 81, 'title': 'The Algorithm Design Manual', 'author': 'Steven S. Skiena', 'description': 'A comprehensive guide to algorithm design.', 'image': 'https://placekitten.com/200/380'},

    {'id': 82, 'title': 'Introduction to Machine Learning', 'author': 'Ethem Alpaydin', 'description': 'An overview of machine learning concepts.', 'image': 'https://placekitten.com/200/381'},

    {'id': 83, 'title': 'Computer Graphics: Principles and Practice', 'author': 'John F. Hughes et al.', 'description': 'A foundational text on computer graphics.', 'image': 'https://placekitten.com/200/382'},

    {'id': 84, 'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell and Peter Norvig', 'description': 'Comprehensive introduction to AI.', 'image': 'https://placekitten.com/200/383'},

    {'id': 85, 'title': 'The Clean Coder', 'author': 'Robert C. Martin', 'description': 'A code of conduct for professional programmers.', 'image': 'https://placekitten.com/200/384'},

    {'id': 86, 'title': 'Compilers: Principles, Techniques, and Tools', 'author': 'Alfred V. Aho et al.', 'description': 'A foundational text on compiler design.', 'image': 'https://placekitten.com/200/385'},

    {'id': 87, 'title': 'Computer Architecture: A Quantitative Approach', 'author': 'John L. Hennessy and David A. Patterson', 'description': 'In-depth study of computer architecture.', 'image': 'https://placekitten.com/200/386'},

    {'id': 88, 'title': 'Machine Learning: A Probabilistic Perspective', 'author': 'Kevin P. Murphy', 'description': 'An introduction to probabilistic machine learning.', 'image': 'https://placekitten.com/200/387'},

    {'id': 89, 'title': 'Data Mining: Concepts and Techniques', 'author': 'Jiawei Han et al.', 'description': 'A comprehensive guide to data mining techniques.', 'image': 'https://placekitten.com/200/388'},

    {'id': 90, 'title': 'Introduction to Information Retrieval', 'author': 'Christopher D. Manning et al.', 'description': 'A comprehensive guide to information retrieval.', 'image': 'https://placekitten.com/200/389'},

    {'id': 91, 'title': 'Computer Security: Principles and Practice', 'author': 'William Stallings and Lawrie Brown', 'description': 'A comprehensive guide to computer security.', 'image': 'https://placekitten.com/200/390'},

    {'id': 92, 'title': 'Digital Design and Computer Architecture', 'author': 'David Harris and Sarah Harris', 'description': 'A comprehensive guide to digital design.', 'image': 'https://placekitten.com/200/391'},

    {'id': 93, 'title': 'The Algorithm Design Manual', 'author': 'Steven S. Skiena', 'description': 'A comprehensive guide to algorithm design.', 'image': 'https://placekitten.com/200/392'},

    {'id': 94, 'title': 'Introduction to Machine Learning', 'author': 'Ethem Alpaydin', 'description': 'An overview of machine learning concepts.', 'image': 'https://placekitten.com/200/393'},

    {'id': 95, 'title': 'Computer Graphics: Principles and Practice', 'author': 'John F. Hughes et al.', 'description': 'A foundational text on computer graphics.', 'image': 'https://placekitten.com/200/394'},

    {'id': 96, 'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell and Peter Norvig', 'description': 'Comprehensive introduction to AI.', 'image': 'https://placekitten.com/200/395'},

    {'id': 97, 'title': 'The Clean Coder', 'author': 'Robert C. Martin', 'description': 'A code of conduct for professional programmers.', 'image': 'https://placekitten.com/200/396'},

    {'id': 98, 'title': 'Compilers: Principles, Techniques, and Tools', 'author': 'Alfred V. Aho et al.', 'description': 'A foundational text on compiler design.', 'image': 'https://placekitten.com/200/397'},

    {'id': 99, 'title': 'Computer Architecture: A Quantitative Approach', 'author': 'John L. Hennessy and David A. Patterson', 'description': 'In-depth study of computer architecture.', 'image': 'https://placekitten.com/200/398'},

    {'id': 100, 'title': 'Machine Learning: A Probabilistic Perspective', 'author': 'Kevin P. Murphy', 'description': 'An introduction to probabilistic machine learning.', 'image': 'https://placekitten.com/200/399'}
]

@app.route('/')
def index():
    return "Welcome to the E-Library! API is working."

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/api/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '').lower()
    filtered_books = [book for book in books if query in book['title'].lower() or query in book['author'].lower()]
    return jsonify(filtered_books)

@app.route('/api/borrow/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify({"message": f"You have borrowed '{book['title']}' by {book['author']}"})
    else:
        return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)