# Ejercicio guiado: Crear tu proyecto Django 'workshop' y la aplicación 'core'

1. **Crear el proyecto:**
   - Abre tu terminal y ejecuta:
   ```bash
     django-admin startproject workshop
     cd workshop
   ```
2. **Crear la aplicación:**
   - Dentro del directorio del proyecto, ejecuta:
     ```bash
     python manage.py startapp core
     ```
3. **Registrar la app:**
   - Abre `workshop/settings.py` y agrega `'core'` en la lista `INSTALLED_APPS`.

4. **Organizar templates y static:**
   - Dentro de la carpeta `core`, crea las carpetas `templates/core/` y `static/core/`.

5. **Ejecutar servidor:**
   - En la terminal, ejecuta:
   ```bash
   python manage.py runserver
   ```

- Abre tu navegador en `http://127.0.0.1:8000/` para verificar que el servidor está activo.

6. **Crear migraciones iniciales:**
   - Ejecuta:

     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

7. Acceder a Django Admin:
   - Crea un superusuario con:

   ```bash
   python manage.py createsuperuser
   ```

   - Luego accede a `http://127.0.0.1:8000/admin/` para iniciar sesión.

**Consejos:**

- Usa un entorno virtual para aislar dependencias.
- Mantén un archivo `requirements.txt` con las librerías usadas.

---

Este ejercicio te permitirá aplicar los conceptos aprendidos y sentar una base sólida para el desarrollo profesional con Django.
