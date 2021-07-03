# TP-RSA
## Objectif du projet
Cette application en ligne de commande permet de communiquer en RSA. Elle a entièrement été codée from scratch.

## Installation
`pip install primesieve`  
`pip install sympy`

## Exemples d'utilisation:
Le fichier *script_Windows_Linux.txt* contient un exemple de script complet à lancer pour :

 - Générer une paire de clé
 - Écrire un message dans un fichier texte
 - Chiffrer ce message
 - Écrire le résultat du déchiffrement dans un fichier
 - Afficher le fichier de résultat
 
 

Afficher l'aide avec la syntaxe  
`python main.py help`

Générer une paire de clé RSA avec des noms de fichier par défaut  
`python main.py keygen`

Chiffrer un message avec la clé publique  
`python main.py crypt nom_clé.pub "Message à chiffrer"`

Déchiffrer un message avec la clé privée  
`python main.py decrypt nom_clé.priv Message_A_Dechiffrer`

## Options

### Génération de clé
Générer une paire de clé RSA avec des noms de fichier définis (ne pas mettre d'extension pour le nom de fichier)  
`python main.py keygen -f nom_clé`

Générer une paire de clé RSA avec des noms de fichier par défaut en définissant la taille des clés  
`python main.py keyge -s taille_clé`

### Chiffrement de message

Chiffrer un message avec la clé publique à partir d'un fichier  
`python main.py crypt nom_clé.pub -i nom_fichier_a_chiffrer`

Chiffrer un message avec la clé publique et mettre le résultat dans un fichier  
`python main.py crypt nom_clé.pub "Message à chiffrer" -o nom_fichier_cible`

### Déchiffrement de message

Déchiffrer un message avec la clé privée à partir d'un fichier  
`python main.py decrypt nom_clé.priv -i nom_fichier_a_dechiffrer`

Déchiffrer un message avec la clé publique et mettre le résultat dans un fichier  
`python main.py decrypt nom_clé.priv "Message à déchiffrer" -o nom_fichier_cible`

### Combinaison d'options
Générer une paire de clé RSA avec des noms personnalisés en définissant la taille des clés  
`python main.py keygen -f nom_clé -s taille_clé`

On peut cumuler plusieurs options par exemple:  
`python main.py crypt nom_clé.pub -i nom_fichier_a_chiffrer -o nom_fichier_cible`
