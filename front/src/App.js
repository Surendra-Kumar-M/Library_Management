// Filename: src/Books.js

import React, { Component } from "react";
import axios from "axios";

class Books extends Component {
  state = {
    books: [],
    title: "",
    author: "",
    genre: "",
    publication_year: "",
    available_copies: 0,
    isbn_number: "",
    rating: 1,
    isEditing: true,
    editingBookId: null,
  };

  // Fetch books from API when component mounts
  componentDidMount() {
    this.fetchBooks();
  }

  // Fetch books from the Django backend API
  fetchBooks = () => {
    axios
      .get("http://127.0.0.1:8000/test/")
      .then((res) => {
        this.setState({
          books: res.data,
        });
      })
      .catch((err) => {
        console.error("Error fetching books:", err);
      });
  };

  // Handle form input changes
  handleInputChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  // Handle form submit (Add or Edit book)
  handleSubmit = (e) => {
    e.preventDefault();

    const { title, author, genre, publication_year, available_copies, isbn_number, rating, isEditing, editingBookId } = this.state;

    const bookData = {
      title,
      author,
      genre,
      publication_year: parseInt(publication_year),
      available_copies: parseInt(available_copies),
      isbn_number,
      rating: parseInt(rating),
    };

    if (isEditing) {
      // Update book
      axios
        .put(`http://127.0.0.1:8000/test/${editingBookId}/`, bookData)
        .then(() => {
          this.setState({ isEditing: false, editingBookId: null });
          this.fetchBooks(); // Refresh book list
        })
        .catch((err) => console.error("Error updating book:", err));
    } else {
      // Create new book
      axios
        .post("http://127.0.0.1:8000/test/", bookData)
        .then(() => {
          this.fetchBooks(); // Refresh book list
          this.setState({
            title: "",
            author: "",
            genre: "",
            publication_year: "",
            available_copies: 0,
            isbn_number: "",
            rating: 1,
          });
        })
        .catch((err) => console.error("Error adding book:", err));
    }
  };

  // Handle edit button click
  handleEdit = (book) => {
    this.setState({
      isEditing: true,
      editingBookId: book.id,
      title: book.title,
      author: book.author,
      genre: book.genre,
      publication_year: book.publication_year,
      available_copies: book.available_copies,
      isbn_number: book.isbn_number,
      rating: book.rating,
    });
  };

  // Handle delete button click
  handleDelete = (bookId) => {
    axios
      .delete(`http://0.0.0.1:8000/test/${bookId}/`)
      .then(() => {
        this.fetchBooks(); // Refresh book list
      })
      .catch((err) => console.error("Error deleting book:", err));
  };

  render() {
    return (
      <div className="container">
        <h1>Book List</h1>

        <form onSubmit={this.handleSubmit}>
          <div className="form-group">
            <label>Title</label>
            <input
              type="text"
              name="title"
              className="form-control"
              value={this.state.title}
              onChange={this.handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Author</label>
            <input
              type="text"
              name="author"
              className="form-control"
              value={this.state.author}
              onChange={this.handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Genre</label>
            <select
              name="genre"
              className="form-control"
              value={this.state.genre}
              onChange={this.handleInputChange}
              required
            >
              <option value="Fiction">Fiction</option>
              <option value="Non-Fiction">Non-Fiction</option>
              <option value="Sci-Fi">Sci-Fi</option>
              <option value="Biography">Biography</option>
            </select>
          </div>
          <div className="form-group">
            <label>Publication Year</label>
            <input
              type="number"
              name="publication_year"
              className="form-control"
              value={this.state.publication_year}
              onChange={this.handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Available Copies</label>
            <input
              type="number"
              name="available_copies"
              className="form-control"
              value={this.state.available_copies}
              onChange={this.handleInputChange}
            />
          </div>
          <div className="form-group">
            <label>ISBN Number</label>
            <input
              type="text"
              name="isbn_number"
              className="form-control"
              value={this.state.isbn_number}
              onChange={this.handleInputChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Rating</label>
            <select
              name="rating"
              className="form-control"
              value={this.state.rating}
              onChange={this.handleInputChange}
            >
              {[1, 2, 3, 4, 5].map((rating) => (
                <option key={rating} value={rating}>
                  {rating}
                </option>
              ))}
            </select>
          </div>
          <button type="submit" className="btn btn-primary">
            {this.state.isEditing ? "Update Book" : "Add Book"}
          </button>
        </form>

        <hr />

        <h2>Books</h2>
        <ul className="list-group">
          {this.state.books.map((book) => (
            <li key={book.id} className="list-group-item">
              <h5>{book.title}</h5>
              <p>Author: {book.author}</p>
              <p>Genre: {book.genre}</p>
              <p>Year: {book.publication_year}</p>
              <p>Available Copies: {book.available_copies}</p>
              <p>Rating: {book.rating}</p>
              <button
                className="btn btn-info"
                onClick={() => this.handleEdit(book)}
              >
                Edit
              </button>
              <button
                className="btn btn-danger ml-2"
                onClick={() => this.handleDelete(book.id)}
              >
                Delete
              </button>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default Books;
