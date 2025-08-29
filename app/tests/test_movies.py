import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services import movie_service  

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_db():
    movie_service.movies_db.clear()
    movie_service.current_id = 1


def test_create_movie():
    response = client.post("/movies/", json={"title": "Inception", "rating": 5})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Inception"
    assert data["rating"] == 5
    assert "id" in data


def test_get_movies():
    client.post("/movies/", json={"title": "Matrix", "rating": 4})
    response = client.get("/movies/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Matrix"
    assert data[0]["rating"] == 4


def test_get_movie_by_id():
   
    create_resp = client.post("/movies/", json={"title": "Avatar", "rating": 8})
    movie_id = create_resp.json()["id"]

  
    response = client.get(f"/movies/{movie_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == movie_id
    assert data["title"] == "Avatar"
    assert data["rating"] == 8

  
    not_found_resp = client.get("/movies/999")
    assert not_found_resp.status_code == 404
    assert not_found_resp.json()["detail"] == "Movie not found"


def test_update_movie():
    create_resp = client.post("/movies/", json={"title": "OldTitle", "rating": 3})
    movie_id = create_resp.json()["id"]

    update_resp = client.put(f"/movies/{movie_id}", json={"title": "NewTitle", "rating": 5})
    assert update_resp.status_code == 200
    data = update_resp.json()
    assert data["title"] == "NewTitle"
    assert data["rating"] == 5


def test_delete_movie():
    create_resp = client.post("/movies/", json={"title": "DeleteMe", "rating": 2})
    movie_id = create_resp.json()["id"]

    delete_resp = client.delete(f"/movies/{movie_id}")
    assert delete_resp.status_code == 200
    assert delete_resp.json()["message"] == "Movie deleted successfully"

   
    get_resp = client.get("/movies/")
    assert all(movie["id"] != movie_id for movie in get_resp.json())
