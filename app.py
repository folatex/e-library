from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)



books = [
    {  'id': 1,
        'title': 'Introduction to the Theory of Computation',
        'author': 'Michael Sipser ',
        'description': 'Covers the fundamentals of computation theory.',
        'image': 'library.jpeg',
        'link': 'Introduction-To-The-Theory-Of-Computation-Michael-Sipser.pdf' },
    {'id': 2, 'title': 'Clean Code', 'author': 'Robert C. Martin', 'description': 'A Handbook of Agile Software Craftsmanship.', 'image': 'https://spin.atomicobject.com/wp-content/uploads/Clean-Code.jpg','link': 'https://www.scribd.com/document/768715748/Clean-Code' },
    {'id': 3, 'title': 'The Pragmatic Programmer', 'author': 'Andrew Hunt and David Thomas', 'description': 'Tips and techniques for software development.', 'image': 'https://i.pinimg.com/736x/81/21/dc/8121dc48ec937ecf919bc2c54aa961a4.jpg', 'link': 'https://www.google.com.ng/books/edition/The_Pragmatic_Programmer/5wBQEp6ruIAC?hl=en&gbpv=0'},
    {'id': 4, 
     'title': 'Design Patterns: Elements of Reusable Object-Oriented Software', 'author': 'Erich Gamma et al.', 'description': 'A guide to software design patterns.', 'image': 'https://i.pinimg.com/736x/82/bf/dc/82bfdc2debbb46293e2c2444c4311c05.jpg','link':'chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/http://www.uml.org.cn/c++/pdf/DesignPatterns.pdf'},
    {'id': 5, 'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell and Peter Norvig', 'description': 'Comprehensive introduction to AI.', 'image': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1385600294i/27543.jpg', 'link': 'https://api.pageplace.de/preview/DT0400.9781292401171_A41586057/preview-9781292401171_A41586057.pdf'},
    {'id': 6, 'title': 'The Art of Computer Programming', 'author': 'Donald E. Knuth', 'description': 'A comprehensive monograph on algorithms.', 'image': 'https://i.pinimg.com/236x/5d/a4/cd/5da4cd3778cb614187631dddcdcab13e.jpg', 'link':'https://kolegite.com/EE_library/books_and_lectures/%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%B8%D1%80%D0%B0%D0%BD%D0%B5/The_Art_of_Computer_Programming/The%20Art%20of%20Computer%20Programming%2C%20Vol.%201%20Fundamental%20Algorithms%2C%203rd%20Edition%20%28Donald%20E.%20Knuth%29%20%28z-lib.org%29.pdf'},
    {'id': 7, 'title': 'Code Complete', 'author': 'Steve McConnell', 'description': 'A practical guide to software construction.', 'image': 'https://i.pinimg.com/736x/b8/d3/94/b8d394bd7b2ad0f783defb456539b4f9.jpg', 'link':'https://people.engr.tamu.edu/slupoli/notes/ProgrammingStudio/supplements/Code%20Complete%202nd.pdf'},
    {'id': 8, 'title': 'Introduction to Algorithms', 'author': 'Thomas H. Cormen et al.', 'description': 'Comprehensive textbook on algorithms.', 'image': 'https://i.pinimg.com/236x/ae/59/71/ae59717fdd24226216c7254b8cb7ee4d.jpg', 'link':'https://enos.itcollege.ee/~japoia/algorithms/GT/Introduction_to_algorithms-3rd%20Edition.pdf'},
    {'id': 9, 'title': 'Computer Networking: A Top-Down Approach', 'author': 'James Kurose and Keith Ross', 'description': 'Introduction to computer networking.', 'image': 'https://i.pinimg.com/236x/65/14/83/651483ae04b9a7eeeff7d23d84670302.jpg', 'link':'https://broman.dev/download/Computer%20Networking:%20A%20Top-Down%20Approach%206th%20Edition.pdf'},
    {'id': 10, 'title': 'The Mythical Man-Month', 'author': 'Frederick P. Brooks Jr.', 'description': 'Reflections on software engineering management.', 'image': 'https://i.pinimg.com/236x/ea/be/fc/eabefc814242964193ef6f6feba4f8bf.jpg', 'link':'https://web.eecs.umich.edu/~weimerw/2018-481/readings/mythical-man-month.pdf'},
    {'id': 11, 'title': 'You Don\'t Know JS', 'author': 'Kyle Simpson', 'description': 'A series on JavaScript programming.', 'image': 'https://i.pinimg.com/236x/7b/ae/16/7bae16bb4dbe673a0a00f5a6e7474bbc.jpg', 'link':'https://bnadventure.com/wp-content/uploads/2023/09/You-Dont-Know-JS-Yet-Kyle-Simpson-You-Dont-Know-JS-Yet_-Get-Started-Leanpub-2020.pdf'},
    {'id': 12, 'title': 'Deep Learning', 'author': 'Ian Goodfellow et al.', 'description': 'Comprehensive guide to deep learning.', 'image': 'https://i.pinimg.com/236x/db/89/91/db8991cd9d485d07d02d9209a0edfb6a.jpg', 'link':'https://isip.piconepress.com/courses/temple/ece_4822/resources/books/Deep-Learning-with-PyTorch.pdf'},
    {'id': 13, 'title': 'Computer Vision: Algorithms and Applications', 'author': 'Richard Szeliski', 'description': 'A comprehensive guide to computer vision.', 'image': 'https://i.pinimg.com/236x/6e/28/0c/6e280c840710ece56967c966bfbd7481.jpg', 'link':'https://library.huree.edu.mn/data/202295/2024-06-03/Computer%20Vision%20-%20Algorithms%20and%20Applications%202nd%20Edition,%20Richard%20Szeliski.pdf'},
    {'id': 14, 'title': 'The Clean Coder', 'author': 'Robert C. Martin', 'description': 'A code of conduct for professional programmers.', 'image': 'https://i.pinimg.com/236x/d2/7c/d0/d27cd0352bbd519eeaf1c27e6633f782.jpg', 'link':'https://ptgmedia.pearsoncmg.com/images/9780137081073/samplepages/0137081073.pdf'},
    {'id': 15, 'title': 'Introduction to Machine Learning', 'author': 'Ethem Alpaydin', 'description': 'An overview of machine learning concepts.', 'image': 'https://i.pinimg.com/236x/25/56/15/255615fa24b149bf220b56ab11f7fa9a.jpg', 'link':'https://ai.stanford.edu/~nilsson/MLBOOK.pdf'},
    {'id': 16, 'title': 'Artificial Intelligence for Humans', 'author': 'Jeff Heaton', 'description': 'An introduction to AI concepts.', 'image': 'https://i.pinimg.com/236x/02/0d/3b/020d3bc29513501a8c634749b71df35a.jpg', 'link':'https://www.dcpehvpm.org/E-Content/BCA/BCA-III/artificial_intelligence_tutorial.pdf'},
    {'id': 17, 'title': 'Computer Architecture: A Quantitative Approach', 'author': 'John L. Hennessy and David A. Patterson', 'description': 'In-depth study of computer architecture.', 'image': 'https://i.pinimg.com/736x/2b/e5/39/2be5398da13addfba06a07d45500e969.jpg', 'link':'https://acs.pub.ro/~cpop/SMPA/Computer%20Architecture%20A%20Quantitative%20Approach%20(5th%20edition).pdf'},
    {'id': 18, 'title': 'The Algorithm Design Manual', 'author' : 'Jeffrey S. Vitter', 'description': 'A comprehensive guide to algorithm design.', 'image': 'https://i.pinimg.com/236x/56/8c/66/568c6624df04dcc059b243e1349e1889.jpg', 'link':'https://mimoza.marmara.edu.tr/~msakalli/cse706_12/SkienaTheAlgorithmDesignManual.pdf'},

    {'id': 19, 'title': 'Elements of Programming Interviews', 'author': 'Adnan Aziz et al.', 'description': 'A guide to programming interview questions.', 'image': 'https://i.pinimg.com/236x/b2/43/80/b2438060ef4695ab08371bb5d1bd9c77.jpg', 'link':'https://inprogrammer.com/wp-content/uploads/2022/01/Adnan-Aziz-Tsung-Hsien-Lee-Amit-Prakash-Elements-of-Programming-Interviews-in-Java_-The-Insiders-Guide-2016-CreateSpace-Independent-Publishing-Platform-libgen.lc_.pdf'},

    {'id': 20, 'title': 'Introduction to the Theory of Computation', 'author': 'Michael Sipser', 'description': 'Fundamentals of computation theory.', 'image': 'https://i.pinimg.com/736x/bb/fc/e5/bbfce542dacf19d176f2a50d7b11e12f.jpg', 'link':'https://cglab.ca/~michiel/TheoryOfComputation/TheoryOfComputation.pdf'},

    {'id': 21, 'title': 'Artificial Intelligence: Foundations of Computational Agents', 'author': 'David L. Poole and Alan K. Mackworth', 'description': 'A comprehensive introduction to AI.', 'image': 'https://i.pinimg.com/236x/02/64/01/0264012e54faa4adddccb663ee79a48e.jpg', 'link':'https://nlp.jbnu.ac.kr/AI2019/Cambridge_ArtificialIntelligence.pdf'},

    {'id': 22, 'title': 'Computer Graphics: Principles and Practice', 'author': 'John F. Hughes et al.', 'description': 'A foundational text on computer graphics.', 'image': 'https://i.pinimg.com/474x/23/65/be/2365beb0bd1a5e3539bae9d0cd60ea08.jpg', 'link':'https://ptgmedia.pearsoncmg.com/images/9780321399526/samplepages/0321399528.pdf'},

    {'id': 23, 'title': 'Operating System Concepts', 'author': 'Abraham Silberschatz et al.', 'description': 'A comprehensive guide to operating systems.', 'image': 'https://i.pinimg.com/736x/33/a0/df/33a0df40a063d21499642bb12671e5be.jpg', 'link': 'https://dusithost.dusit.ac.th/~juthawut_cha/download/Operating_System_Concepts_Essentials_2nd_Edition.pdf'},

    {'id': 24, 'title': 'Database System Concepts', 'author': 'Abraham Silberschatz et al.', 'description': 'An introduction to database systems.', 'image': 'https://i.pinimg.com/236x/65/bb/61/65bb61ff28075da728cda25a1d62fc7b.jpg', 'link':'https://people.vts.su.ac.rs/~peti/Baze%20podataka/Literatura/Silberschatz-Database%20System%20Concepts%206th%20ed.pdf'},
    {'id': 25, 'title': 'Computer Networks', 'author': 'Andrew S. Tanenbaum', 'description': 'A comprehensive introduction to networking.', 'image': 'https://i.pinimg.com/236x/75/64/71/75647102b7a429b9902905aa97b77c59.jpg', 'link':'https://vfu.bg/en/e-Learning/Computer-Networks--Introduction_Computer_Networking.pdf'},

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

    {'id': 51, 'title': 'Computer Architecture: A Quantitative Approach', 'author': 'John L. Hennessy and David A. Patterson', 'description': 'In-depth study of computer architecture.', 'image': 'https://i.pinimg.com/736x/eb/3a/ee/eb3aeeaaaf36ca48a2d6adcc062cc909.jpg', 'link':'https://acs.pub.ro/~cpop/SMPA/Computer%20Architecture%20A%20Quantitative%20Approach%20(5th%20edition).pdf'},

    {'id': 52, 'title': 'Machine Learning: A Probabilistic Perspective', 'author': 'Kevin P. Murphy', 'description': 'An introduction to probabilistic machine learning.', 'image': 'https://i.pinimg.com/736x/b1/f8/0c/b1f80c3add6bdad9b7591baf6658c8af.jpg', 'link':'https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/38136.pdf'},

    {'id': 53, 'title': 'Data Mining: Concepts and Techniques', 'author': 'Jiawei Han et al.', 'description': 'A comprehensive guide to data mining techniques.', 'image': 'https://i.pinimg.com/736x/72/ad/49/72ad496ce49fac4852b6b4f20a158332.jpg', 'link':'https://myweb.sabanciuniv.edu/rdehkharghani/files/2016/02/The-Morgan-Kaufmann-Series-in-Data-Management-Systems-Jiawei-Han-Micheline-Kamber-Jian-Pei-Data-Mining.-Concepts-and-Techniques-3rd-Edition-Morgan-Kaufmann-2011.pdf'},

    {'id': 54, 'title': 'Introduction to Information Retrieval', 'author': 'Christopher D. Manning et al.', 'description': 'A comprehensive guide to information retrieval.', 'image': 'https://i.pinimg.com/736x/c2/0b/d5/c20bd533fa83d1bb73065a96fa3b4dbd.jpg', 'link':'https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf'},

    {'id': 55, 'title': 'Computer Security: Principles and Practice', 'author': 'William Stallings and Lawrie Brown', 'description': 'A comprehensive guide to computer security.', 'image': 'https://i.pinimg.com/736x/b5/14/e8/b514e8538f31874547bf013ad7a86e30.jpg', 'link':'https://unidel.edu.ng/focelibrary/books/Computer%20Security%20_%20Principles%20-%20WILLIAM%20STALLINGS_2089.pdf'},

    {'id': 56, 'title': 'Digital Design and Computer Architecture', 'author': 'David Harris and Sarah Harris', 'description': 'A comprehensive guide to digital design.', 'image': 'https://i.pinimg.com/736x/a0/bb/45/a0bb450a401cf5e9b21fb07b3d4de3fc.jpg', 'link':'https://www.r-5.org/files/books/computers/hw-layers/hardware/digital-desigh/David_Harris_Sarah_Harris-Digital_Design_and_Computer_Architecture-EN.pdf'},

    {'id': 57, 'title': 'The Algorithm Design Manual', 'author': 'Steven S. Skiena', 'description': 'A comprehensive guide to algorithm design.', 'image': 'https://i.pinimg.com/736x/9f/a5/43/9fa5437da1047d180b46d2a5c86ac51a.jpg', 'link':'https://mimoza.marmara.edu.tr/~msakalli/cse706_12/SkienaTheAlgorithmDesignManual.pdf'},

    {'id': 58, 'title': 'Introduction to Machine Learning', 'author': 'Ethem Alpaydin', 'description': 'An overview of machine learning concepts.', 'image': 'https://i.pinimg.com/736x/4c/71/32/4c7132cee99bdc4631ba570c9ba7dcb2.jpg', 'link':'https://dl.matlabyar.com/siavash/ML/Book/(Adaptive%20computation%20and%20machine%20learning)%20Ethem%20Alpaydin-Introduction%20to%20machine%20learning-MIT%20Press%20(2004).pdf'},

    {'id': 59, 'title': 'Computer Graphics: Principles and Practice', 'author': 'John F. Hughes et al.', 'description': 'A foundational text on computer graphics.', 'image': 'https://i.pinimg.com/736x/23/65/be/2365beb0bd1a5e3539bae9d0cd60ea08.jpg', 'link':'https://ptgmedia.pearsoncmg.com/images/9780321399526/samplepages/0321399528.pdf'},

    {'id': 60, 'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell and Peter Norvig', 'description': 'Comprehensive introduction to AI.', 'image': 'https://i.pinimg.com/736x/2c/d3/26/2cd32698f424d893e2c7600f69c5612d.jpg', 'link':'http://repo.darmajaya.ac.id/4836/1/Stuart%20Russell%2C%20Peter%20Norvig-Artificial%20Intelligence_%20A%20Modern%20Approach-Prentice%20Hall%20%28%20PDFDrive%20%29.pdf'},

    {'id': 61, 'title': 'The Clean Coder', 'author': 'Robert C. Martin', 'description': 'A code of conduct for professional programmers.', 'image': 'https://i.pinimg.com/736x/e0/a7/3b/e0a73b1f864cb1986112efef5b9f3a68.jpg', 'link':'https://ptgmedia.pearsoncmg.com/images/9780137081073/samplepages/0137081073.pdf'},

    {'id': 62, 'title': 'Compilers: Principles, Techniques, and Tools', 'author': 'Alfred V. Aho et al.', 'description': 'A foundational text on compiler design.', 'image': 'https://i.pinimg.com/736x/86/ef/a3/86efa31b18b7bfd29b97a9d11c87efca.jpg', 'link':'https://ggnindia.dronacharya.info/Downloads/Sub-info/RelatedBook/6thSem/Compiler-Design-TEXT-book-1.pdf'},

    {'id': 63, 'title': 'Computer Architecture: A Quantitative Approach', 'author': 'John L. Hennessy and David A. Patterson', 'description': 'In-depth study of computer architecture.', 'image': 'https://i.pinimg.com/736x/97/ce/52/97ce52347a136c9700e3a83ce8647265.jpg', 'link':'https://www.cse.iitd.ac.in/~rijurekha/col216/quantitative_approach.pdf'},

    {'id': 64, 'title': 'Machine Learning: A Probabilistic Perspective', 'author': 'Kevin P. Murphy', 'description': 'An introduction to probabilistic machine learning.', 'image': 'https://i.pinimg.com/736x/7e/61/cc/7e61cc93ccbeca8d1cb544db2328e5d0.jpg', 'link':'https://www.cs.ubc.ca/~murphyk/MLbook/pml-toc-1may12.pdf'},

    {'id': 65, 'title': 'Data Mining: Concepts and Techniques', 'author': 'Jiawei Han et al.', 'description': 'A comprehensive guide to data mining techniques.', 'image': 'https://i.pinimg.com/736x/ed/3b/7f/ed3b7fc5e84c9d2c82b8fb0504c4477c.jpg', 'link':'https://myweb.sabanciuniv.edu/rdehkharghani/files/2016/02/The-Morgan-Kaufmann-Series-in-Data-Management-Systems-Jiawei-Han-Micheline-Kamber-Jian-Pei-Data-Mining.-Concepts-and-Techniques-3rd-Edition-Morgan-Kaufmann-2011.pdf'},

    {'id': 66, 'title': 'Introduction to Information Retrieval', 'author': 'Christopher D. Manning et al.', 'description': 'A comprehensive guide to information retrieval.', 'image': 'https://i.pinimg.com/736x/59/a4/f6/59a4f66c74b6db0663b3e909000a1878.jpg', 'link':'https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf'},

    {'id': 67, 'title': 'Computer Security: Principles and Practice', 'author': 'William Stallings and Lawrie Brown', 'description': 'A comprehensive guide to computer security.', 'image': 'https://i.pinimg.com/736x/6e/06/5a/6e065aa46a7019c381ca141c3606ee9a.jpg', 'link':'https://www.pearsonhighered.com/assets/preface/0/1/3/2/0132775069.pdf'},

    {'id': 68, 'title': 'Digital Design and Computer Architecture', 'author': 'David Harris and Sarah Harris', 'description': 'A comprehensive guide to digital design.', 'image': 'https://i.pinimg.com/736x/e1/d2/97/e1d297b1786232e86405d9ac4db208ea.jpg', 'link':'https://www.r-5.org/files/books/computers/hw-layers/hardware/digital-desigh/David_Harris_Sarah_Harris-Digital_Design_and_Computer_Architecture-EN.pdf'},

    {'id': 69, 'title': 'The Algorithm Design Manual', 'author': 'Steven S. Skiena', 'description': 'A comprehensive guide to algorithm design.', 'image': 'https://i.pinimg.com/736x/56/e7/86/56e7861784fed4669a0a87c1ca2561e7.jpg', 'link':'https://mimoza.marmara.edu.tr/~msakalli/cse706_12/SkienaTheAlgorithmDesignManual.pdf'},

    {'id': 70, 'title': 'Introduction to Machine Learning', 'author': 'Ethem Alpaydin', 'description': 'An overview of machine learning concepts.', 'image': 'https://i.pinimg.com/736x/e2/7f/d4/e27fd4c6f6069fcd3e838b444943334c.jpg', 'link':'https://dl.matlabyar.com/siavash/ML/Book/(Adaptive%20computation%20and%20machine%20learning)%20Ethem%20Alpaydin-Introduction%20to%20machine%20learning-MIT%20Press%20(2004).pdf'},

    {'id': 71, 'title': 'Computer Graphics: Principles and Practice', 'author': 'John F. Hughes et al.', 'description': 'A foundational text on computer graphics.', 'image': 'https://i.pinimg.com/736x/2a/13/42/2a134291facbff3875534fb0fa55325a.jpg', 'link':'http://students.aiu.edu/submissions/profiles/resources/onlineBook/a6A8H5_computer%20graphics.pdf'},

    {'id': 72, 'title': 'Artificial Intelligence: A Modern Approach', 'author': 'Stuart Russell and Peter Norvig', 'description': 'Comprehensive introduction to AI.', 'image': 'https://i.pinimg.com/736x/1b/95/15/1b9515b67ba7ee613b28a840acb66750.jpg', 'link':'http://lib.ysu.am/disciplines_bk/b7707dde83ee24b2b23999b4df5fd988.pdf'},

    {'id': 73, 'title': 'The Clean Coder', 'author': 'Robert C. Martin', 'description': 'A code of conduct for professional programmers.', 'image': 'https://i.pinimg.com/736x/f8/64/5e/f8645e92e5613eb320bd589d74e69e26.jpg', 'link':'https://ptgmedia.pearsoncmg.com/images/9780137081073/samplepages/0137081073.pdf'},

    {'id': 74, 'title': 'Compilers: Principles, Techniques, and Tools', 'author': 'Alfred V. Aho et al.', 'description': 'A foundational text on compiler design.', 'image': 'https://i.pinimg.com/736x/ee/bf/ba/eebfbab59fb613f2a3100bc6e581af1a.jpg', 'link':'https://ggnindia.dronacharya.info/Downloads/Sub-info/RelatedBook/6thSem/Compiler-Design-TEXT-book-1.pdf'},

    {'id': 75, 'title': 'Computer Architecture: A Quantitative Approach', 'author': 'John L. Hennessy and David A. Patterson', 'description': 'In-depth study of computer architecture.', 'image': 'https://i.pinimg.com/736x/1d/cc/20/1dcc20c47deb3031fb127c3e4e74fce3.jpg', 'link':'https://acs.pub.ro/~cpop/SMPA/Computer%20Architecture%20A%20Quantitative%20Approach%20(5th%20edition).pdf'},

    {'id': 76, 'title': 'Machine Learning: A Probabilistic Perspective', 'author': 'Kevin P. Murphy', 'description': 'An introduction to probabilistic machine learning.', 'image': 'https://i.pinimg.com/736x/75/fc/8e/75fc8e96c1f19f9477295376135931a8.jpg', 'link':'https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/38136.pdf'},

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
    
@app.route('/api/books/<int:book_id>/pdf', methods=['GET'])
def serve_pdf(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book and 'pdf_link' in book:
        pdf_file_path = book['pdf_link']
        # Ensure the file exists before sending it
        if os.path.exists(pdf_file_path):
            return send_file(pdf_file_path, mimetype='application/pdf')
        else:
            return jsonify({"message": "PDF file not found"}), 404
    else:
        return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
