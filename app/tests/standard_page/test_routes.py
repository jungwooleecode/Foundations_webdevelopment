#testing success

def test_index_success(client):
  # Page loads
  response = client.get('/')
  assert response.status_code == 200

def test_about_success(client):
  # Page loads
  response = client.get('/about')
  assert response.status_code == 200

def test_workshops_success(client):
    # Page loads
    response = client.get('/workshops')
    assert response.status_code == 200

def test_classinfo_success(client):
  # Page loads
  response = client.get('/classinfo')
  assert response.status_code == 200

def test_bookingcomplete_success(client):
  # Page loads
  response = client.get('/bookingcomplete')
  assert response.status_code == 200

def test_book_success(client):
  # Page loads
  response = client.get('/book')
  assert response.status_code == 200

def test_reset_success(client):
  # Page loads
  response = client.get('/reset')
  assert response.status_code == 200

def test_register_success(client):
  # Page loads
  response = client.get('/register')
  assert response.status_code == 200

def test_mailbox_success(client):
  # Page loads
  response = client.get('/mailbox')
  assert response.status_code == 200

def test_login_success(client):
  # Page loads
  response = client.get('/login')
  assert response.status_code == 200

def test_forgot_success(client):
  # Page loads
  response = client.get('/forgot')
  assert response.status_code == 200

def test_mypage_success(client):
  # Page loads
  response = client.get('/mypage/<int:id>')
  assert response.status_code == 200

#testing content

def test_index_content(client):
  # Returns welcome text
  response = client.get('/')
  assert b'Welcome to summer 2022 global dance workshops!' in response.data