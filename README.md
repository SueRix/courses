<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <nav class="navbar navbar-dark bg-dark">
        <div class="container">
            <a href={% url "shop:index" %} class="navbar-brand">Courses Shop</a>
            <span class="navbar-text">
                <a href="/admin/" class="me-2" target="_blank">Admin</a>
                <a href="/api/v1/" target="_blank">API</a>
            </span>
        </div>
    </nav>
    <main class="container">
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>
