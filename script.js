// frontend/script.js

// Fetch books from the Flask backend
async function fetchBooks() {
    const response = await fetch('http://127.0.0.1:5000/api/books');
    const books = await response.json();
    displayBooks(books);
}

// Display books dynamically
function displayBooks(filteredBooks) {
    const bookList = document.getElementById('book-list');
    bookList.innerHTML = ''; // Clear the current list

    filteredBooks.forEach(book => {
        const bookDiv = document.createElement('div');
        bookDiv.classList.add('book');
        bookDiv.innerHTML = `
            <img src="${book.image}" alt="${book.title}">
            <h3>${book.title}</h3>
            <p>${book.author}</p>
            <p>${book.description}</p>
            <a href="${book.pdf_link}" target="_blank">
                <button id="button-book-${book.id}">Read Pdf</button>
            </a>
        `;
        bookList.appendChild(bookDiv);

        // Add an event listener to the button
        const button = document.getElementById(`button-book-${book.id}`);
        button.addEventListener('click', function(event) {
            // Prevent the default action of the anchor tag
            event.preventDefault();
            // Show the alert
            window.alert(`You have borrowed "${book.title}" written by ${book.author} from the E-library.`);
            // Optionally, you can also redirect to the PDF link after the alert
            window.open(book.link, '_blank');
        });
    });
}
// Borrow book by sending a POST request
async function borrowBook(bookId) {
    const response = await fetch(`http://127.0.0.1:5000/api/borrow/${bookId}`, {
        method: 'POST',
    });
    const data = await response.json();
    alert(data.message); // Show borrowing message
}

// Search books based on the query
async function searchBooks() {
    const query = document.getElementById('search-bar').value.toLowerCase();
    const response = await fetch(`http://127.0.0.1:5000/api/search?query=${query}`);
    const filteredBooks = await response.json();
    displayBooks(filteredBooks);
}

// Initialize the library on page load
fetchBooks();
