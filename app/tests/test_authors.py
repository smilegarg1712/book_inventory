from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_author():
    response = client.post("/authors/", json={"name": "J.K. Rowling", "biography": "Author of Harry Potter"})
    assert response.status_code == 200
    assert response.json()["name"] == "J.K. Rowling"

def test_get_authors():
    response = client.get("/authors/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_author():
    # First, create an author
    create_response = client.post("/authors/", json={"name": "George Orwell", "biography": "Author of 1984"})
    assert create_response.status_code == 200
    author_id = create_response.json()["id"]

    # Then, retrieve the author
    response = client.get(f"/authors/{author_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "George Orwell"

def test_update_author():
    # First, create an author
    create_response = client.post("/authors/", json={"name": "J.K. Rowling", "biography": "Author of Harry Potter"})
    author_id = create_response.json()["id"]

    # Then, update the author
    response = client.put(f"/authors/{author_id}", json={"name": "J.K. Rowling", "biography": "Updated biography"})
    assert response.status_code == 200
    assert response.json()["biography"] == "Updated biography"

def test_delete_author():
    # First, create an author
    create_response = client.post("/authors/", json={"name": "Ernest Hemingway", "biography": "Author of The Old Man and the Sea"})
    author_id = create_response.json()["id"]

    # Then, delete the author
    delete_response = client.delete(f"/authors/{author_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Author deleted successfully"}

    # Try to get the deleted author
    response = client.get(f"/authors/{author_id}")
    assert response.status_code == 404
