# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define g = Character('Gwen', color="#c8ffc8")
image gwen = "Gwen.png"
image cv = "cv.jpg"
image bg = "bg.jpg"


# Le jeu commence ici
label start:

    scene cv
    with dissolve
    show gwen at left
    with dissolve

    g "Bienvenu sur le CV Game !"
    g "Vous allez découvrir mon parcours au fur et mesure tout en vous amusant !"
    g "Je vous souhaite une agréable partie !"

    scene bg
    with dissolve
    show gwen at left
    with dissolve

    g"Bien maintenant je vais vous laisser choisir"
    g"Par quoi voulez-vous commencer ?"
    
    show screen formation
    show screen competences
    show screen profil
    call screen parcours

return
