# Backend MedicAI

## Getting start for developer

### Install postgresql 

```bash
psql -U postgres -h localhost
CREATE DATABASE backend_medicai;

psql -U postgres -h localhost -f init.sql
```

### Install python and setup environment

```bash
# Install Python  3.9
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate

# Run unit test
pytest
```

### Generate jwt secret

```bash
import secrets

# Generate a secure random secret key
secret_key = secrets.token_hex(32)
print(secret_key)
```

### Database migration

```bash
# Run only the first time
flask db init

# Create migration
flask db migrate -m "Initial migration."

# Run to upgrade the database
flask db upgrade
```
