import os
import django
from django.utils import timezone

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canacintra.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Categoria, Tag, Post, Comentario, Suscriptor

def seed():
    print("Iniciando carga de datos de ejemplo...")
    
    # 1. Crear superusuario (admin)
    if not User.objects.filter(username='admin').exists():
        admin_user = User.objects.create_superuser('admin', 'admin@canacintra.com', 'admin123')
        print("Superusuario creado con éxito.")
        print("  Usuario: admin")
        print("  Contraseña: admin123")
    else:
        admin_user = User.objects.get(username='admin')
        print("El usuario 'admin' ya existe.")
        
    # 2. Crear categorías
    cat_datos = [
        {"nombre": "Innovación Industrial", "descripcion": "Últimas tendencias en automatización, robótica y tecnología industrial."},
        {"nombre": "Capacitación Empresarial", "descripcion": "Cursos, talleres y programas para potenciar las habilidades de tu equipo."},
        {"nombre": "Eventos y Congresos", "descripcion": "Mantente al tanto de nuestros próximos congresos, networking y exposiciones corporativas."},
        {"nombre": "Noticias Nacionales", "descripcion": "Acontecimientos clave, políticas económicas y comerciales que impactan a la industria mexicana."}
    ]
    
    categorias = {}
    for cat in cat_datos:
        c, creado = Categoria.objects.get_or_create(
            nombre=cat["nombre"],
            defaults={"descripcion": cat["descripcion"]}
        )
        categorias[cat["nombre"]] = c
        if creado:
            print(f"Categoría creada: {cat['nombre']}")
            
    # 3. Crear etiquetas
    tag_datos = ["Pymes", "Tecnología", "Manufactura", "Liderazgo", "Sustentabilidad"]
    tags = {}
    for tag in tag_datos:
        t, creado = Tag.objects.get_or_create(nombre=tag)
        tags[tag] = t
        if creado:
            print(f"Etiqueta creada: {tag}")
            
    # 4. Crear Publicaciones (Posts)
    post_datos = [
        {
            "titulo": "El Impacto de la Inteligencia Artificial en la Manufactura Mexicana",
            "contenido": """La manufactura inteligente o Industria 4.0 está transformando radicalmente la productividad de las plantas industriales en México. 
            
A través de la integración de algoritmos de Inteligencia Artificial (IA) y sensores IoT, las fábricas son ahora capaces de predecir fallas en la maquinaria con días de anticipación, optimizar la cadena de suministro en tiempo real y reducir el desperdicio de materiales hasta en un 30%.
            
Canacintra está liderando iniciativas clave de capacitación y vinculación para que las pequeñas y medianas empresas (Pymes) locales puedan adoptar estas tecnologías disruptivas sin necesidad de realizar inversiones multimillonarias iniciales. El futuro de la competitividad nacional reside en la digitalización de nuestros procesos productivos.""",
            "resumen": "Descubre cómo las Pymes y grandes industrias mexicanas están adoptando tecnologías de Inteligencia Artificial para optimizar procesos y liderar la Industria 4.0.",
            "categoria": categorias["Innovación Industrial"],
            "tags_asociados": ["Tecnología", "Manufactura", "Pymes"],
            "destacado": True
        },
        {
            "titulo": "Próximo Congreso Nacional de Negocios Canacintra 2026",
            "contenido": """Nos complace anunciar la fecha oficial del Congreso Nacional de Negocios Canacintra 2026, el punto de encuentro anual más relevante para el sector industrial de nuestro país.
            
Este año el evento se centrará en 'Liderazgo Sostenible y Resiliencia en las Cadenas de Suministro'. Contaremos con la participación de ponentes internacionales de primer nivel, mesas de debate sobre políticas de nearshoring y un piso de exposición comercial donde más de 200 empresas ofrecerán soluciones de vanguardia.
            
Las inscripciones ya están abiertas con tarifas preferenciales para todos nuestros afiliados activos. ¡Reserva tu lugar hoy mismo!""",
            "resumen": "Anunciamos las fechas y temas centrales del Congreso Nacional de Negocios 2026. Paneles sobre nearshoring, ponentes internacionales y networking premium.",
            "categoria": categorias["Eventos y Congresos"],
            "tags_asociados": ["Liderazgo", "Sustentabilidad"],
            "destacado": False
        },
        {
            "titulo": "Programas de Sustentabilidad y Economía Circular para el 2026",
            "contenido": """La sustentabilidad ha dejado de ser un tema opcional para convertirse en un pilar estratégico de supervivencia empresarial. Las nuevas normativas nacionales e internacionales exigen que las industrias adopten modelos de producción mucho más limpios.
            
En Canacintra lanzamos el nuevo programa de certificación en 'Economía Circular', diseñado especialmente para ayudar a las plantas manufactureras a rediseñar sus ciclos de vida de productos, reducir la huella de carbono corporativa y generar ahorros operativos significativos a través del reciclaje de subproductos industriales.
            
El programa cuenta con becas del 50% patrocinadas por organismos internacionales de desarrollo sustentable.""",
            "resumen": "Lanzamiento del programa de certificación de Economía Circular Canacintra. Métricas de huella de carbono y becas disponibles para socios.",
            "categoria": categorias["Capacitación Empresarial"],
            "tags_asociados": ["Sustentabilidad", "Manufactura"],
            "destacado": True
        }
    ]
    
    posts = []
    for post in post_datos:
        p, creado = Post.objects.get_or_create(
            titulo=post["titulo"],
            defaults={
                "contenido": post["contenido"],
                "resumen": post["resumen"],
                "autor": admin_user,
                "categoria": post["categoria"],
                "publicado": True,
                "destacado": post["destacado"],
                "fecha_publicacion": timezone.now()
            }
        )
        
        # Asociar tags
        for t_nombre in post["tags_asociados"]:
            p.tags.add(tags[t_nombre])
            
        posts.append(p)
        if creado:
            print(f"Publicación creada: {post['titulo']}")
            
    # 5. Crear Comentarios
    comentario_datos = [
        {
            "post": posts[0],
            "autor": admin_user,
            "contenido": "Excelente artículo. Las Pymes realmente necesitan apoyo en la adopción tecnológica para no quedarse atrás en el nearshoring.",
            "aprobado": True
        },
        {
            "post": posts[0],
            "autor": admin_user,
            "contenido": "Me interesa mucho la certificación de Industria 4.0. ¿Tienen fechas para el siguiente webinar informativo?",
            "aprobado": True
        },
        {
            "post": posts[1],
            "autor": admin_user,
            "contenido": "Ya reservé mi boleto de afiliado para el Congreso. El panel de nearshoring promete bastante este año.",
            "aprobado": True
        },
        {
            "post": posts[2],
            "autor": admin_user,
            "contenido": "Muy buena iniciativa. ¿El curso de economía circular estará disponible en formato online para otros estados?",
            "aprobado": False # Comentario sin moderar para probar el panel de moderación del admin
        }
    ]
    
    for com in comentario_datos:
        c, creado = Comentario.objects.get_or_create(
            post=com["post"],
            autor=com["autor"],
            contenido=com["contenido"],
            defaults={"aprobado": com["aprobado"]}
        )
        if creado:
            estado = "aprobado" if com["aprobado"] else "pendiente de revisión"
            print(f"Comentario agregado en '{com['post'].titulo}' ({estado})")
            
    # 6. Crear Suscriptores
    sub_datos = ["juan.perez@example.com", "maria.lopez@example.com", "contacto@empresa.com"]
    for sub in sub_datos:
        s, creado = Suscriptor.objects.get_or_create(email=sub)
        if creado:
            print(f"Suscriptor de boletín creado: {sub}")
            
    print("\n¡Carga de datos de ejemplo completada perfectamente!")
    print("--------------------------------------------------")
    print("Acceso al Admin Django:")
    print("  URL: http://127.0.0.1:8000/admin/")
    print("  Usuario: admin")
    print("  Contraseña: admin123")
    print("--------------------------------------------------")

if __name__ == '__main__':
    seed()
