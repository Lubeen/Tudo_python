from app import create_app #Poucos tests

def test_api_is_ok(app):
    app = create_app()
    with app.test_client() as client:
        response = client.get('/api')
        assert response.status_code == 200
        assert 'Bruno' in str(response.data)