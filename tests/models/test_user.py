from src.models.user import User


def test_new_user():
    user = User(email='testuser@gmail.com', password='password')
    assert user.email == 'testuser@gmail.com'
    assert user.password == 'password'
