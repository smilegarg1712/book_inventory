from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_genre():
    response = client.post("/genres/", json={"name": "Fantasy"})
    assert response.status_code == 200
    assert response.json()["name"] == "Fantasy"

def test_get_genres():
    response = client.get("/genres/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_genre():
    # First, create a genre
    create_response = client.post("/genres/", json={"name": "Science Fiction"})
    assert create_response.status_code == 200
    genre_id = create_response.json()["id"]

    # Then, retrieve the genre
    response = client.get(f"/genres/{genre_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Science Fiction"

def test_update_genre():
    # First, create a genre
    create_response = client.post("/genres/", json={"name": "Horror"})
    genre_id = create_response.json()["id"]

    # Then, update the genre
    response = client.put(f"/genres/{genre_id}", json={"name": "Thriller"})
    assert response.status_code == 200
    assert response.json()["name"] == "Thriller"

def test_delete_genre():
    # First, create a genre
    create_response = client.post("/genres/", json={"name": "Romance"})
    genre_id = create_response.json()["id"]

    # Then, delete the genre
    delete_response = client.delete(f"/genres/{genre_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Genre deleted successfully"}

    # Try to get the deleted genre
    response = client.get(f"/genres/{genre_id}")
    assert response.status_code == 404
