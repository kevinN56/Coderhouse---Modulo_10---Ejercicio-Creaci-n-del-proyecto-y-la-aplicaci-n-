# 📚 Blog Django

Este es un proyecto web desarrollado con Django que permite gestionar posts, autores y etiquetas (tags). Incluye un sistema de administración personalizado y relaciones entre modelos.

---

## 🚀 Características

- CRUD de Posts
- Gestión de Autores
- Sistema de Tags (ManyToMany)
- Panel de administración personalizado
- Validaciones en modelos
- URLs dinámicas con `get_absolute_url()`

---

## 🧰 Tecnologías utilizadas

- Python 3.x
- Django 4.x
- SQLite (base de datos por defecto)

---

## ⚙️ Instalación del proyecto

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

# Proyecto Blog - CRUD de Posts con Django

## Descripción

Este proyecto fue desarrollado con Django e implementa un sistema completo de gestión de publicaciones (Posts) utilizando vistas basadas en clases (Class-Based Views).

El sistema permite realizar las operaciones básicas de un CRUD (Create, Read, Update, Delete) sobre el modelo `Post`.

## Funcionalidades implementadas

### Listado de publicaciones (ListView)

Se implementó una vista que muestra todos los posts almacenados en la base de datos. Las publicaciones se presentan ordenadas por fecha de publicación de forma descendente, mostrando primero las más recientes.

### Detalle de publicación (DetailView)

Permite visualizar toda la información de una publicación específica, incluyendo su título, contenido, fecha de publicación y autor.

### Creación de publicaciones (CreateView)

Los usuarios autenticados pueden crear nuevas publicaciones mediante un formulario basado en el modelo `Post`.

### Edición de publicaciones (UpdateView)

Permite modificar los datos de una publicación existente, actualizando la información almacenada en la base de datos.

### Eliminación de publicaciones (DeleteView)

Permite eliminar una publicación del sistema mediante una página de confirmación previa para evitar borrados accidentales.

## Rutas principales

| URL                  | Descripción                |
| -------------------- | -------------------------- |
| `/post/list/`        | Lista de publicaciones     |
| `/post/<id>/`        | Detalle de una publicación |
| `/post/new/`         | Crear publicación          |
| `/post/<id>/edit/`   | Editar publicación         |
| `/post/<id>/delete/` | Eliminar publicación       |

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML

## Cómo ejecutar el proyecto

1. Clonar el repositorio.
2. Crear y activar un entorno virtual.
3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:

```bash
python manage.py migrate
```

5. Ejecutar el servidor:

```bash
python manage.py runserver
```

6. Acceder desde el navegador a:

```text
http://127.0.0.1:8000/
```

## Pruebas realizadas

Se verificó correctamente el funcionamiento de las operaciones CRUD:

- Creación de publicaciones.
- Visualización de publicaciones.
- Edición de publicaciones existentes.
- Eliminación de publicaciones.
- Navegación entre las distintas vistas mediante enlaces y URLs configuradas.

# Comparación entre FBVs y CBVs en Django

## Introducción

Django ofrece dos formas principales de crear vistas: las vistas basadas en funciones (Function-Based Views o FBVs) y las vistas basadas en clases (Class-Based Views o CBVs). Ambas permiten responder a las solicitudes de los usuarios, pero difieren en la forma en que organizan el código y reutilizan funcionalidades.

## Function-Based Views (FBVs)

Las FBVs son funciones de Python que reciben un objeto `request` y devuelven una respuesta. Son fáciles de entender y adecuadas para lógica simple.

Ejemplo utilizado en este proyecto:

```python
def home(request):
    return render(request, 'core/index.html')
```

Esta vista renderiza la página principal y resulta sencilla de implementar porque solo necesita mostrar una plantilla.

### Ventajas de las FBVs

- Más simples para principiantes.
- Mayor control sobre el flujo de ejecución.
- Adecuadas para lógica personalizada y específica.

### Desventajas de las FBVs

- Requieren escribir más código para operaciones repetitivas.
- Menor reutilización de funcionalidades.
- Pueden volverse difíciles de mantener en proyectos grandes.

## Class-Based Views (CBVs)

Las CBVs utilizan clases y herencia para proporcionar funcionalidades predefinidas. Django incluye clases genéricas para operaciones comunes como listar, crear, actualizar y eliminar registros.

En este proyecto se utilizaron CBVs para implementar el CRUD del modelo `Post`:

```python
class PostListView(LoginRequiredMixin, ListView):
    model = Post
```

```python
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
```

```python
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
```

```python
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
```

```python
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
```

Estas clases permiten implementar funcionalidades complejas con pocas líneas de código.

### Ventajas de las CBVs

- Mayor reutilización de código.
- Menor cantidad de código repetido.
- Facilitan la implementación de operaciones CRUD.
- Integración sencilla con mixins como `LoginRequiredMixin`.

### Desventajas de las CBVs

- Curva de aprendizaje más alta.
- Puede resultar menos intuitivo entender la herencia y los métodos internos.
- La personalización avanzada requiere conocer la estructura de las clases.

## Conclusión

En este proyecto se utilizó una FBV para la página principal debido a su simplicidad, mientras que las operaciones CRUD del modelo `Post` fueron implementadas mediante CBVs. Esta decisión permitió aprovechar las ventajas de las vistas genéricas de Django, reduciendo la cantidad de código necesario y mejorando la organización y mantenibilidad del proyecto.
