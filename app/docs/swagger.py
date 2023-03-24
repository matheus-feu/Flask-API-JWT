template = {
    "swagger": "2.0",
    "info": {
        "title": "Flask API para CRUD de usuários",
        "description": "Esta API foi desenvolvida para fins de estudo e aprendizado.",

        "contact": {
            "email": "matheusfeu@gmail.com",
            "url": "https://www.linkedin.com/in/matheus-feu-558558186/",
        },
        "version": "v1.0.0"
    },
    "basePath": "/api/v1/",
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "APIKeyHeader": {
            "type": "apiKey",
            "name": "x-access-token",
            "in": "header",
            "description": "Authorization header using the APIKeyHeader scheme. Example: \"Authorization: APIKeyHeader {token}\""
        }
    },
}


swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs"
}