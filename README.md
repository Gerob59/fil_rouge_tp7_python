
# fil_rouge_tp7_python

## Description
Ce projet fil-rouge a été réalisé dans le cadre de notre alternance en tant que data-engineers chez Diginamic. Il s'agit d'une application RESTful développée en Python 3.11, utilisant plusieurs librairies et frameworks pour différentes fonctionnalités.

## Fonctionnalités
- L'application utilise le framework FastAPI pour créer une API RESTful performante.
- Elle se connecte à une base de données MySQL à l'aide de la librairie pyMySQL.
- La gestion de l'ORM est assurée par la librairie SqlAlchelmy.
- Les tests unitaires sont mis en place avec le module unittest.
- Pour les besoins de certaines fonctionnalités, nous utilisons la librairie Selenium.
- Le serveur d'application est démarré à l'aide de la librairie Uvicorn.

## Architecture du Projet
Le projet suit une structure standard pour un projet Python. Voici un aperçu :
```
nom_projet/
    |- README.md
    |- requirements.txt
    |- setup.py
    |- .gitignore
    |- projet/
        |- __init__.py
        |- main.py
        |- controllers/
            |- __init__.py
            |- ...
        |- models/
            |- __init__.py
            |- ...
        |- routes/
            |- __init__.py
            |- ...
        |- schemas/
            |- __init__.py
            |- ...
    |- tests/
        |- __init__.py
        |- ...
    |- docs/
        |- documentation.md
    |- config/
        |- __init__.py
        |- db.py
        |- ...

```
- Le dossier `projet/` contient le code source de l'application, avec ses différents modules.
- Les tests unitaires sont placés dans le dossier `tests/`.
- Les fichiers de documentation se trouvent dans les dossiers `docs/` et `docs_tech/`.

## Installation
1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir **Python 3.11** installé sur votre système.
3. Créez un environnement virtuel et activez-le.
4. À l'intérieur de l'environnement virtuel, exécutez la commande suivante pour installer les dépendances du projet :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation
1. Assurez-vous que votre environnement virtuel est activé.
2. Accédez au répertoire du projet.
3. Exécutez la commande suivante pour démarrer le serveur d'application :
   ```bash
   uvicorn projet.main:app --reload
   ```
   Cela lancera le serveur d'application sur `http://localhost:8000`.

## Contributions
Ce projet a été développé par [Fatih Eyili](https://github.com/ftheyili), [Antonin Guillon](https://github.com/AntoninGuillon) et [Robin Hotton](https://github.com/Gerob59).

## Commandes
Ajouter une dépendance au projet :
```bash
pip freeze > requirements.txt
```