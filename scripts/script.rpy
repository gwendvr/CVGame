# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"


# Le jeu commence ici
label start:

    scene cv
    with dissolve
    show gwen at left
    with dissolve

    g "Bonjour à toi !"
    g "Pour commencer puis-je demander votre nom ?"
    $ playerName = renpy.input("Mon nom :" )

    g "Bienvenu %(playerName)s ! Je suis Gwen."

    g "Tu vas découvrir mon parcours au fur et mesure tout en t'amusant !"
    g "Je te souhaite une agréable partie !"

    scene bg
    with dissolve
    show gwen at left
    with dissolve

    g"Bien maintenant je vais te laisser choisir"
    g"Par quoi veux-tu commencer ?"
    
    show screen formation
    show screen competences
    show screen profil
    call screen parcours

return
