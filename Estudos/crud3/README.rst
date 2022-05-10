#Como rodar esse projeto

#experiencia com um crud usando flaskk e suas ferramentas

- flask
- flask-sqlalchemy
- flask-migrate
- flask-marshmallow
- marshmallow_sqlalchemy



```sh
export FLASK_APP=crud3/app.py
export FLASK_ENV=development
export FLASK_DEBUG=True

flask run
```

## como fazer as migrações

    ```sh
    flask db init
    flask db migrate 
    flask db upgrade
    ```