# Docker/Sqlalchemy/Oracle Project Template

Life is short, use Python3 and Container Runtimes ...

## Docker Containers

**Start Services**

Add `--build` to rebuild images

```
docker-compose up
```

The oracle database will run at localhost:1521.

**Stop Services**

Add `-v` to clean up volumes

```
docker-compose down
```

## Development

**Attach Python Container**

```
docker exec -it app bash
```

**Environment Variables**

We use a environment file `.env` at root folder to configure our app. The python package `environ` is used for parsing these variables.

**Project Configurations**

The configurations file is `settings.py` at package folder.

**Sqlalchemy Interface**

```
>>> from app.database.utils import session_scope
>>> with session_scope('default') as session:
>>>     # Do your ORM stuff with session here!
```

## Test

Run pytest command in the container:
```
pytest -s
```

## Command line tools

The interface is `manage.py` at project folder. 

Make sure you attach the python container before executing them.

* Migrate the schema to default database:

    ```
    >>> python manage.py init --db=default
    OK
    ```

* Describe a table:

    ```
    >>> python manage.py describe --table=person
    {
        "columns": [
            {
                "name": "id",
                "type": "INTEGER",
                "nullable": false,
                "default": null,
                "autoincrement": "auto",
                "comment": null
            },
            {
                "name": "english_name",
                "type": "VARCHAR(120)",
                "nullable": true,
                "default": null,
                "autoincrement": "auto",
                "comment": null
            },
            {
                "name": "chinese_name",
                "type": "VARCHAR(120)",
                "nullable": true,
                "default": null,
                "autoincrement": "auto",
                "comment": null
            }
        ],
        "check_constraints": [],
        "foreign_keys": [],
        "indexes": [],
        "pk_constraint": {
            "constrained_columns": [
                "id"
            ],
            "name": "sys_c0011644"
        },
        "primary_keys": [
            "id"
        ],
        "table_comment": {
            "text": null
        }
    }
    ```