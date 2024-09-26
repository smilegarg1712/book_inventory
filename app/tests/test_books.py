from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#stClient(app)

# Test for creating a book
def test_create_book():
    response = client.post("/books/", json={
        "title": "Test Book"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

# Test for getting all books
def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test for getting a specific book
def test_get_book():
    response = client.get("/books/1")  # Assuming the first book has ID 1
    assert response.status_code == 200
    assert "title" in response.json()

# Test for updating a book
def test_update_book():
    update_data = {"title": "Updated Book", "author": "Updated Author"}
    response = client.put("/books/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == update_data["title"]

# Test for deleting a book
def test_delete_book():
    response = client.delete("/books/1")  # Assuming the first book has ID 1
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted successfully"

# Test for getting a non-existent book
def test_get_nonexistent_book():
    response = client.get("/books/999")  # Assuming this ID doesn't exist
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"

# Test for deleting a non-existent book
def test_delete_nonexistent_book():
    response = client.delete("/books/999")  # Assuming this ID doesn't exist
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"
