import uuid

import flask

from app.routes import CARTS

HTTP_OK = 200


def test_session_id_creation(client, app):
    """Test that a session ID is created when visiting the site."""
    with client:
        response = client.get("/cart")
        assert response.status_code == HTTP_OK

        assert "session_id" in flask.session
        assert uuid.UUID(flask.session["session_id"], version=4)


def test_session_persistence(client, app):
    """Test that the session ID persists across requests."""
    with client:
        first_response = client.get("/cart")
        assert first_response.status_code == HTTP_OK
        first_session_id = flask.session["session_id"]

        second_response = client.get("/cart")
        assert second_response.status_code == HTTP_OK
        second_session_id = flask.session["session_id"]

        assert first_session_id == second_session_id


def test_cart_operations_use_session_id(client):
    """Test that cart operations manipulate the cart tied to the session."""
    with client:
        client.get("/add/1")
        session_id = flask.session["session_id"]

        assert session_id in CARTS
        assert len(CARTS[session_id]["items"]) == 1

        client.get("/remove/1")
        assert CARTS[session_id]["items"] == []
