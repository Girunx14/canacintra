# 📋 Contexto del Proyecto - Canacintra Blog de Noticias

## 🎯 Descripción del Proyecto
Sitio web de noticias tipo blog desarrollado con **Django 6.0** y **MariaDB**, diseñado para la publicación y gestión de contenido noticioso del sector industrial.

## 🏗️ Arquitectura Técnica

### Stack Tecnológico
- **Framework**: Django 6.0 (última versión estable)
- **Base de Datos**: MariaDB/MySQL
- **Driver**: PyMySQL
- **Frontend**: Bootstrap 5.3, Google Fonts (Newsreader + Roboto)
- **Despliegue**: MySQL Workbench para gestión de BD

### Estructura del Proyecto
```
canacintra/
├── canacintra/         # Configuración principal del proyecto
│   ├── __init__.py     # Inicialización PyMySQL
│   ├── settings.py     # Configuración Django
│   ├── urls.py         # Ruteo principal
│   └── wsgi.py         # WSGI config
├── blog/               # App de noticias
│   ├── models.py       # Modelos: Post, Categoria, Tag, Comentario
│   ├── views.py        # Vistas del blog
│   ├── admin.py        # Admin Django configurado
│   ├── forms.py        # Formularios
│   └── templates/blog/ # Templates del blog
├── accounts/           # App de autenticación
│   ├── views.py        # Login, registro, perfil
│   ├── urls.py         # Rutas de cuentas
│   └── templates/accounts/ # Templates de auth
├── templates/          # Templates base
│   └── base.html       # Template base con diseño UI/UX
├── database.sql        # Script SQL inicial
├── .env                # Variables de entorno
└── requirements.txt    # Dependencias
```

## 🎨 Design System (UI/UX Pro Max)

### Tipografía
- **Headings**: Newsreader (serif, editorial)
- **Body**: Roboto (sans-serif, legibilidad)
- **Escala**: 12px, 14px, 16px, 18px, 20px, 24px, 32px, 40px

### Colores
```css
--color-primary: #18181B    /* Negro editorial */
--color-secondary: #3F3F46  /* Gris secundario */
--color-accent: #0066CC     /* Azul institucional */
--color-background: #FAFAFA /* Fondo claro */
--color-border: #E4E4E7     /* Bordes sutiles */
```

### Espaciado (8pt Grid)
- xs: 4px, sm: 8px, md: 16px, lg: 24px, xl: 32px, 2xl: 48px, 3xl: 80px

### Accesibilidad (WCAG 2.1 AA)
- ✅ Contrast 4.5:1 mínimo
- ✅ Touch targets 44x44px
- ✅ Focus states visibles
- ✅ Skip links
- ✅ ARIA labels
- ✅ Reduced motion support

## 📦 Modelos de Datos

### Post
- título, slug, contenido, autor (FK User)
- categoria (FK), tags (M2M), imagen_portada
- resumen, publicado, destacado
- fecha_creacion, fecha_actualizacion, fecha_publicacion

### Categoria
- nombre, slug, descripcion

### Tag
- nombre, slug

### Comentario
- post (FK), autor (FK User), contenido
- aprobado (moderación), fecha_creacion

## 🔐 Autenticación
- Registro de usuarios con Django auth
- Login/Logout
- Perfil de usuario
- Moderación de comentarios (aprobado/no aprobado)

## 🛠️ Funcionalidades Implementadas

### Blog
- ✅ Listado de noticias con paginación
- ✅ Detalle de noticia con breadcrumbs
- ✅ Filtrado por categoría y tag
- ✅ Noticias relacionadas
- ✅ Sistema de comentarios con moderación
- ✅ Búsqueda (pendiente)
- ✅ Galería de imágenes (pendiente)

### Usuario
- ✅ Registro e inicio de sesión
- ✅ Perfil de usuario
- ✅ Panel de estadísticas
- ✅ Historial de publicaciones

### Admin (Django Admin)
- ✅ CRUD completo de publicaciones
- ✅ Moderación de comentarios (aprobar/desaprobar)
- ✅ Gestión de categorías y tags
- ✅ Filtros y búsquedas

## 📱 Responsive Design
- Mobile-first approach
- Breakpoints: 375px, 768px, 1024px, 1440px
- Touch-friendly (44px min)
- Landscape support

## 🚀 Comandos de Desarrollo

```bash
# Entorno virtual
source venv/bin/activate

# Migrar base de datos
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Servidor de desarrollo
python manage.py runserver

# Recoger estáticos (producción)
python manage.py collectstatic
```

## 📋 Variables de Entorno (.env)
```env
SECRET_KEY='tu-clave-secreta'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=canacintra_db
DB_USER=canacintra_user
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
```

## ✅ Pre-Entrega Checklist (UI/UX Pro Max)

### Accesibilidad
- [x] No emojis como iconos (usar SVG/Bootstrap Icons)
- [x] Focus states visibles
- [x] Touch targets 44px+
- [x] Contrast 4.5:1+
- [x] ARIA labels
- [x] Skip links
- [x] Reduced motion support

### Interacción
- [x] Hover states 150-300ms
- [x] Loading feedback
- [x] Disabled states claros
- [x] Cursor pointer en clickable

### Layout
- [x] Mobile-first
- [x] Responsive 375px-1440px
- [x] 8pt grid system
- [x] Safe areas

### Performance
- [x] Font-display: swap
- [x] Lazy loading imágenes
- [x] Critical CSS inline

## 📚 Referencias
- [Django Docs](https://docs.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickstart/)
- [Material Design](https://material.io/design)
- [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/)

## 🔄 Flujo de Trabajo para IA

Cuando trabajes en este proyecto:

1. **Lee este AGENTS.md** para contexto
2. **Revisa las skills** en `.agents/skills/` (django-expert, frontend-design, ui-ux-pro-max)
3. **Mantén consistencia** con el design system establecido
4. **Respeta accesibilidad** (WCAG 2.1 AA)
5. **Prueba responsive** en todos los breakpoints
6. **Commit en español** descriptivo

## 📞 Contacto
- **Email**: contacto@canacintra.org
- **Teléfono**: (55) 1234-5678

---

**Última actualización**: Mayo 2024
**Versión**: 1.0.0
