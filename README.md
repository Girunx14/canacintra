# Canacintra - Blog de Noticias

Sitio web de noticias tipo blog desarrollado con Django y MariaDB.

## Requisitos Previos

- Python 3.10+
- MariaDB/MySQL Server
- MySQL Workbench (opcional, para gestionar la BD)

## Instalación

### 1. Crear base de datos

Ejecuta el script `database.sql` en MySQL Workbench o desde la consola:

```bash
mysql -u root -p < database.sql
```

O copia el contenido del archivo SQL y ejecútalo en MySQL Workbench.

### 2. Instalar dependencias

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Edita el archivo `.env` con tus credenciales de base de datos:

```env
DB_NAME=canacintra_db
DB_USER=canacintra_user
DB_PASSWORD=tu_contraseña_segura
DB_HOST=localhost
DB_PORT=3306
```

### 4. Migrar la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario (admin)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Visita `http://localhost:8000/admin` para acceder al panel de administración.

## Estructura del Proyecto

```
canacintra/
├── canacintra/         # Configuración del proyecto
│   ├── __init__.py     # Inicialización PyMySQL
│   ├── settings.py     # Configuración principal
│   ├── urls.py         # URLs principales
│   └── wsgi.py         # WSGI config
├── blog/               # App de noticias
├── accounts/           # App de autenticación
├── database.sql        # Script SQL inicial
├── .env                # Variables de entorno
└── requirements.txt    # Dependencias
```

## Modelos del Blog

El proyecto incluye los siguientes modelos:

- **Categoria**: Clasificación principal de las notas
- **Tag**: Etiquetas para las publicaciones  
- **Post**: Publicaciones del blog con título, contenido, autor, categoría, tags, imagen, etc.

## Próximos Pasos

- ~~[Paso 2]~~ ✅ Modelos del Blog (Post, Categoría, Tag)
- [Paso 3] Autenticación de usuarios
- [Paso 4] Vistas y Templates del Blog
- [Paso 5] Sistema de Comentarios
