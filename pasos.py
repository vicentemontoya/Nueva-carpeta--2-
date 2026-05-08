# Pasos a seguir para subir un proyecto a GitHub

# 0. (Solo la primera vez) configurar tu identidad en git:
#    git config --global user.name "Tu Nombre"
#    git config --global user.email "tu@email.com"

# 1. Crear la carpeta del proyecto
# 2. Abrir la carpeta en VS Code
# 3. Abrir la terminal y poner: git init
# 4. Crear un archivo README.md (opcional pero recomendado)
# 5. Poner: git add .              (agrega todos los archivos)
#    o:    git add README.md       (solo el README)
# 6. Poner: git commit -m "inicio"
# 7. Poner: git status              (verifica que todo se trackeó bien)
# 8. Poner: git branch -M main      (renombra la rama principal a "main")

# --- En GitHub.com ---
# 9. Crear un repositorio nuevo y vacío en github.com (sin README)
#    y copiar la URL que te entrega.

# --- De vuelta en la terminal ---
# 10. Poner: git remote add origin https://github.com/usuario/repo.git
# 11. Poner: git push -u origin main

# Para futuros cambios, el ciclo es:
#   git add .
#   git commit -m "mensaje del cambio"
#   git push
