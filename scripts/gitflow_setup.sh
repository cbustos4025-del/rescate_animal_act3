# Ejecutar:  bash scripts/gitflow_setup.sh
# CAMBIA la URL por la de tu repositorio público en GitHub.
REPO="https://github.com/TU_USUARIO/refugio-animal.git"

git init
git checkout -b master
git add .gitignore README.md
git commit -m "chore: commit inicial con README y .gitignore"
git remote add origin $REPO
git push -u origin master

git checkout -b develop
git push -u origin develop

# --- feature 1: modelo y patrón Factory ---
git checkout -b feature/factory-expedientes develop
git add refugio/models/expedientes.py refugio/patterns/factory.py
git commit -m "feat(factory): expedientes por especie con Factory Method"
git checkout develop
git merge --no-ff feature/factory-expedientes -m "merge: feature/factory-expedientes"

# --- feature 2: Observer ---
git checkout -b feature/observer-notificaciones develop
git add refugio/patterns/observer.py refugio/models/usuarios.py
git commit -m "feat(observer): notificaciones a voluntarios"
git checkout develop
git merge --no-ff feature/observer-notificaciones -m "merge: feature/observer-notificaciones"

# --- feature 3: State + caso ---
git checkout -b feature/state-estados develop
git add refugio/patterns/state.py refugio/models/caso.py
git commit -m "feat(state): ciclo de vida del caso con trazabilidad"
git checkout develop
git merge --no-ff feature/state-estados -m "merge: feature/state-estados"

# --- feature 4: Singleton + MVC ---
git checkout -b feature/singleton-mvc develop
git add refugio main.py
git commit -m "feat(core): Singleton GestorCasos y estructura MVC"
git checkout develop
git merge --no-ff feature/singleton-mvc -m "merge: feature/singleton-mvc"

# --- feature 5: pruebas y documentación ---
git checkout -b feature/pruebas-docs develop
git add tests docs scripts
git commit -m "test/docs: pruebas unitarias y documentación del diseño"
git checkout develop
git merge --no-ff feature/pruebas-docs -m "merge: feature/pruebas-docs"

# --- release a master ---
git checkout -b release/1.0.0 develop
git commit --allow-empty -m "chore(release): version 1.0.0"
git checkout master
git merge --no-ff release/1.0.0 -m "release: v1.0.0"
git tag -a v1.0.0 -m "Version 1.0.0"
git checkout develop
git merge --no-ff release/1.0.0 -m "merge: release/1.0.0 a develop"
git branch -d release/1.0.0

git push origin --all
git push origin --tags
git log --graph --oneline --all
