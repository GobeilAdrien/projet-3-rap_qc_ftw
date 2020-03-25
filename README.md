# Quoridor - Partie 2

<img src="https://python.gel.ulaval.ca/media/notebook/quoridor.png" style="display: block; margin-left: auto; margin-right: auto;" alt="Quoridor" width="50%" height="auto">

## Objectifs

Pour ce deuxième projet, vous aurez à créer une classe pour encapsuler le jeu Quoridor. Vous aurez à réutiliser certain segment de code de votre module `quoridor.py`.

## Prérequis

- [Git](https://git-scm.com/downloads/)
- [Python](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com/download/)

## Extension VS Code

Voici la liste des extensions **VS Code** que nous vous conseillons d'ajouter à votre configuration&thinsp;:

- Python (&thinsp;celui de Microsoft&thinsp;)
- GitLense - Git supercharged
- Live Share Extension Pack
- Bracket Pair Colorizer
- Indent-Rainbow
- autoDocstring

Pour **autoDocstring**, allez ensuite dans la barre de menu en haut à gauche et ensuite dans `Fichier -> Préférences -> Paramètres`, dans la barre de recherche apparaissant dans la fenêtre chercher `Auto Docstring`.
Vous devriez voir un menu déroulant en dessous de **Docstring Format**, choisissez l'option `google`.

## Commandes utile

Démarrer une partie&thinsp;:

``` bash
> python3 main.py votre_idul
```

Lancer le module de test&thinsp;:

``` bash
> python3 test.py
```

*NOTE&thinsp;: Pour lancer le module de test, vous aurez besoin d'installer le module externe `pytest`.*

Installer un module externe **Python**&thinsp;:

``` bash
> pip3 install nom_du_module
```

Créer un bundle&thinsp;:

``` bash
> git bundle create quoridor.bundle HEAD master
```

Vérifier que le bundle a été créé avec succès&thinsp;:

``` bash
> git bundle verify quoridor.bundle
```

Unbundler un bundle&thinsp;:

``` bash
> git clone quoridor.bundle
```

## Liens utile

- [Aide-mémoire Github Git](https://github.github.com/training-kit/downloads/fr/github-git-cheat-sheet.pdf)
- [Documentation Pytest](https://docs.pytest.org/en/latest/) [&thinsp;en anglais&thinsp;]
