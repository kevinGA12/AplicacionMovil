# -- Aplicación Web/Movil --

## Requisitos

- Python 3.11.9 (Debido a que el stack de Heroku solo soporta ciertas versiones de Python) (https://www.python.org/downloads/release/python-3119/)

- Cuenta de Heroku (https://signup.heroku.com/login)

- Heroku CLI (https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli)


- (Opcional) PostgreSQL para ver nuestra base de datos dentro de la CLI (https://www.postgresql.org/download/)

## Deploy
Descargamos la rama main de este repositorio y la guardamos dentro de una carpeta la cual seria nuestro ambiente de trabajo.
Para guiar los comandos, primero debemos referirnos al repositorio local donde tenemos nuestro ambiente de trabajo
- cd (ruta en la cual estaría nuestra aplicación)
Y crear un repositorio de github en lo que seria nuestro nuevo repositorio local
- git init

Al tener nuestro repositorio local, se debe crear una cuenta de 'Heroku' en la cual tendremos nuestra aplicación hosteada al igual que su base de datos que lo acompaña.

Dentro de una CLI debemos ingresar a nuestra cuenta de Heroku en la cual crearemos nuestro proyecto con el siguiente comando y siguiendo sus pasos. Para crear una cuenta ver en 'Requisitos'.
- heroku login  
Luego, debemos crear nuestro proyecto en Heroku con el siguiente comando.
- heroku create <NOMBRE_DEL_PROYECTO>
Subimos todos los archivos de nuestro repositorio local al remoto de Heroku.
- git add .
- git commit -m "Commit inicial"
- git push heroku master (de no funcionar reemplazar master con HEAD:master)
Con esto ya tendríamos el repositorio remoto actualizado con nuestro repositorio local, y se debe elegir ademas el **plan de nuestro web dyno** en la **dashboard** de Heroku, en la pestaña de **Recursos** o **Resources**

Agregamos nuestra base de datos creando un addon relacionado a nuestra aplicación y seleccionar el plan para este.

(Para ver los planes disponibles)
- heroku addons:plans heroku-postgresql
(Aca creamos nuestra base de datos)
- heroku addons:create heroku-postgresql:<PLAN_A_SELECCIONAR> --app <NOMBRE_DEL_PROYECTO>

Finalmente tendremos que realizar las migraciones, crear un superuser, y abrirlo.
- heroku run python manage.py migrate
(Seguir los pasos asociados a crear un superuser)
- heroku run Python manage.py createssuperuser
- heroku open

## Licencia

MIT License

Copyright (c) [2024] [Kevin Guarda]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

