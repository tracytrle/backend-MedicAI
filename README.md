# Backend MedicAI

## Getting start for developer

```bash
# Install Python  3.9
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
```

### Generate jwt secret

```bash
import secrets

# Generate a secure random secret key
secret_key = secrets.token_hex(32)
print(secret_key)
```