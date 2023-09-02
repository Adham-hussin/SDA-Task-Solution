# SDA-Task-Solution
# Book Store Desktop App

This is a book store desktop application developed as a task for the Cairo University Racing Team in the Automation Department. It is implemented using Python and PyQt5. The application allows users to search for books, apply filters, view book details, and make purchases.

## Features

- Search Bar: Enter keywords to search for books by title, author, or section.
- Filter Button: Apply filters to refine search results.
- Search Button: Trigger the search based on the entered keywords and filters.
- Book List View: Display the search results with book titles, authors, sections, and prices.
- Buy Button: Purchase a selected book.
- Checkout Window: Enter name and address for purchasing books.

## Prerequisites

- Python 3.x installed on your system and added to the PATH

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/book-store.git
    ```

2. Create a virtual environment and enter it:

    ```bash
    virtualenv venv
    ```
    ```bash
    venv\Scripts\activate
    ```
3. Install the required libraries:

    You will find them in requirements.txt
4. Run the application:

    ```bash
    python book_store.py
    ```

## Usage

1. Upon running the application, the main window of the book store app will appear.
2. Enter keywords in the search bar to search for books. You can also apply filters using the filter button.
3. Click the search button to perform the search.
4. The list view will display the search results with book titles, authors, sections, and prices.
5. Click on a book to view additional details.
6. Double click to hide additional details.
7. To purchase a book, click the "Buy" button under the book. A checkout window will appear.
8. Enter your name and address in the checkout window and click the "Confirm" button to complete the purchase.
9. You will find your invoice in directory "/invoices"
