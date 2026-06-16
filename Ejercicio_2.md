# Ejercicio práctico: Modelar un blog simple

En este ejercicio, aplicarás lo aprendido para definir modelos que representen un blog con las siguientes entidades y relaciones:

1. **Author (Autor):**
   - Campos: name (CharField, max 100), email (EmailField, único)
   - Método **str** que retorne el nombre

2. **Tag (Etiqueta):**
   - Campo: name (CharField, max 30)
   - Método **str** que retorne el nombre

3. **Post (Publicación):**
   - Campos: title (CharField, max 200), content (TextField), published_date (DateTimeField)
   - Relación: author (ForeignKey a Author, con on_delete=models.CASCADE)
   - Relación: tags (ManyToManyField a Tag)
   - Método **str** que retorne el título
   - Clase Meta para ordenar por fecha de publicación descendente

4. **Validación personalizada:**
   - En el modelo Post, implementar el método clean() para validar que el título contenga al menos 5 caracteres.

**Pasos:**

    - Crea un archivo models.py o usa tu entorno de desarrollo.
    - Define las clases con los campos y relaciones indicados.
    - Implementa los métodos especiales y validaciones.
    - Revisa que la sintaxis sea correcta y que las relaciones reflejen el dominio.

**Reflexión:**

    - ¿Cómo las relaciones entre modelos facilitan consultas complejas?

    - ¿Qué ventajas ofrece implementar validaciones en el modelo frente a hacerlo en la vista?

Este ejercicio te prepara para gestionar migraciones y consultas ORM, que veremos en las próximas unidades.
