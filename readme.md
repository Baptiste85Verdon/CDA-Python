# Jeu de gestion - Python 

## Contexte :
Jeu du type "Clicker" dans le thème du jeu vidéo Minecraft. Le but est simplement de pouvoir générer par clic et de manière automatique de l'or pour ensuite acheter des bonus et faire le meilleur score sans limite de temps.

## Fonctionnalités :
- Génération d'or par clics
  - Au démarrage, lors de chaque clic sur le minerai d'or à droite de l'écran, 1 d'or est généré.
  - Le montant généré est améliorable en achetant certains des bonus présents dans les boutons de gauche.
- Génération d'or automatique
  - Au démarrage, toutes les 10 secondes, 1 d'or est généré automatiquement.
  - Le montant généré est améliorable en achetant certains des bonus présents dans les boutons de gauche.
  - Le temps d'interval entre chaque génération automatique peut être réduit en achetant certains des bonus présents dans les boutons de gauche.
- Achat de bonus
  - Les bonus sont rangés en 3 blocs
    - Le premier concerne des améliorations du nombre d'or généré par clics.
    - Le second concerne des améliorations du nombre d'or généré automatiquement.
    - Le troisième concerne des réductions du temps d'interval entre chaque génération automatique d'or.
  - Chaque bonus possède un prix et un montant de bonus en fonction de ce qu'il va améliorer
  - Certains bonus ont des conditions de débloquage avant de pouvoir être achetés
    - Ils peuvent avoir une condition sur un autre bonus (exemple : Il faut avoir acheté le 1er bonus au moins 5 fois pour débloquer le deuxième)
    - Ils peuvent avoir une condition sur le nombre d'or généré par clic (exemple : Il faut générer au moins 200 d'or par clic)
    - Ils peuvent avoir une condition sur le nombre d'or généré par automatisation (exemple : Il faut générer au moins 500 d'or automatiquement)
    - Ils peuvent avoir une condition sur l'interval entre chaque automatisation (exemple : Il faut avoir un temps entre chaque clic automatique inférieur ou égal à 8s)

## Évolutions :
- Placement des boutons dans un row et non par coordonnées  
- Avoir des bonus qui seraient des multiplicateurs en plus des bonus d'ajouts
- Avoir un moyen de connaître le nombre de clics au total lors d'une partie ainsi que le nombre d'or généré au total (sans soustraire les achats de bonus)
- Avoir un background animé
- Avoir des sons au clic et achats de bonus
- Avoir des bonus structurés avec un titre, une description plus petite en dessous et une image associée (exemple : Titre -> Pioche en fer , Description -> Augmente vos clics de 20 , Image -> Pioche en fer)
- Lors d'un achat de bonus, avoir un endroit qui regroupe les images des différents bonus ainsi qu'un compteur pour savoir combien de fois il a été acheté (exemple : Image de la pioche en fer et son niveau en indice)
- Avoir un menu de jeu cohérent avec le thème et un moyen d'y retourner pour y placer le bouton "Quitter et sauvegarder" à cet endroit
- Avoir un input pour mettre son nom/pseudo lorsqu'on quitte et sauvegarde pour l'avoir dans le fichier score
- Ajouter le nombre de clics total et d'or généré dans le fichier score
- Avoir une page dédiée aux meilleurs scores.