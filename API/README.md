## Configuration de l'API Flask

### Prérequis
- Python 3.x installé
- `pip` pour gérer les dépendances Python
- `npm` pour exécuter les scripts définis dans `package.json`

### Étapes d'installation

1. **Cloner le dépôt** :
   ```bash
   git clone  https://github.com/coderangel117/biblio-handling 
   cd biblio-handling/API
   ```

2. **Installer les dépendances Python** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer les variables d'environnement** :
   Créez un fichier `.env` depuis le `.env.example` et modifiez les variables suivantes :
   ```
   DB_USER=<votre_utilisateur>
   DB_HOST=<hôte_de_la_base_de_données>
   DB_PASSWD=<mot_de_passe>
   DB_NAME=<nom_de_la_base_de_données>
   SECRET_PASS=<clé_secrète>
   ```
   Générer une clé secrète pour JWT :
   ```bash
    python -c "import secrets; print(secrets.token_hex(16))"
    ```
   
4. **Démarrer l'API Flask** :
   Utilisez la commande suivante pour démarrer l'API :
   ```bash
   npm run start
   ```

5. **Tester l'API** :
   Utilisez un outil comme Postman ou `curl` pour tester les routes disponibles.

### Structure du projet

- `API/main.py` : Point d'entrée principal de l'application Flask.
- `API/api/config.py` : Configuration de l'application, y compris la base de données et les clés JWT.
- `API/api/routes/` : Contient les routes de l'API.
- `API/tests/` : Contient les tests unitaires pour l'API.

### Notes
- Assurez-vous que votre base de données est configurée et accessible avant de démarrer l'API.
- Les fichiers sensibles comme `.env` ne doivent pas être inclus dans le contrôle de version.
