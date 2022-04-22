label choix_formation :

        hide screen competences with dissolve
        hide screen profil with dissolve
        scene bg
        show gwen at left

        pause 1.0
        g"Tu as choisi les formations !"
        g"C'est un bon choix car j'ai fais pas mal de formations différentes."
        g"Nous allons commencer par le début, le BAC !"

        show screen bac
        hide screen formation
        g"Je vous présente mon diplôme du BAC : BAC STMG option Marketing."
        g"Juste avant ce BAC j'avais essayé le BAC ST2S."
        g"Sciences et Technologies de la Santé et du Social."
        g"Je voulais faire kiné !"
        g"Mais pour faire ce métier il faut passer par la médecine générale..."
        g"Le problème c'est que j'ai peur du sang !"
        g"Donc je te laisse imaginer quand je suis arrivée à mon premier TP en SVT."

        g"Je me perds là !"
        g"Pour en revenir au BAC STMG, mon but était de créer mon entreprise, il me manquait seulement une idée."
        g"J'ai choisi marketing pour cette raison !"
        g"Tu vois les études de marchés, comment fonctionne le client c'est important !"
        
        hide screen bac with dissolve
        show screen bts with dissolve
        g"Bon, ensuite je suis partie sur un BTS MUC."
        g"Management des Unités Commerciales."
        g"Maintenant je crois que c'est le BTS MCO !"
        g"Encore une réforme !"

        g"J'ai choisi ce BTS car je pouvais apprendre le métier de manageur."
        g"Ce qui est important quand on veut créer une entreprise !"
        g"En plus j'ai pu faire cette formation en alternance !"
        g"Connais-tu l'alternance ?"

        menu:
                "Oui !":
                        jump continuer
                "Non, mais ça ne m'intéresse pas de toute façon !":
                        jump continuer
                "Non, tu peux m'expliquer ?":
                        jump explication

label explication:
        g"C'est un système de formation qui est fondé sur une phase pratique et une phase théorique qui alternent."
        g"L'alternance comprend deux types de contrats : le contrat d'apprentissage et le contrat de professionnalisation. Ces deux contrats permettent de concilier travail en entreprise et formation théorique."
        g"Par exemple, en BTS MUC, je faisais ma formation le lundi, mardi et mercredi, et je travaillais le jeudi et vendredi."
        g"Mais pendant les vancances je travaillais à temps plein dans mon entreprise."
        g"On est aussi salarié de l'entreprise, donc on a 5 semaines de vacances par an."
        g"Enfin l'alternance c'est plein d'avantage, on peut avoir des APL plus avantageux mais aussi plein d'autres aides, comme Mobilijeune qui donne une aide supplémentaire pour le logement."
        jump continuer

label continuer:
        g"Pour revenir sur le BTS, j'ai fais cette formation au lycée du Grésivaudan à Meylan."
        g"J'ai acquis plusieurs compétences :"

        g"Enfin j'ai décidé de refaire un BTS car la filière que j'ai choisi finalement me plaisais pas tant que ça."
        g"J'ai cherché en 2020 après mon BTS ce que je pouvais bien faire."
        g"Et une idée m'es venu."
        g"J'ai décidé de faire de ma passion mon métier !"
        g"J'aime beaucoup écrire des histoires, et créer des petits jeux vidéos comme celui-ci !"
        g"Donc j'ai décider de me former en programmation et de faire un BTS SIO."
        g"Services Informatiques aux Organisations."
        g"Et en plus avec mes formation en commercer j'avais les bases pour aussi créer mon entreprise !"
        
        g"Je voulais aussi faire ce BTS en alternance donc j'ai cherchait et je n'ai pas trouvé pour la première année."
        g"Comme il était trop tard pour s'inscrire en formation initial, j'ai ma formation en distenctiel."
        g"Mais ça correspondait bien avec la période du Covid."
        g"Cette expérience m'a permis à me débrouiller dans mon apprentissage et d'apprendre de nombreux langages de programmation."
        g"Vous pourrez les voir dans la partie compétence !"

        g"Enfin j'ai pu faire ma deuxième année en alternance avec Les charmilles et l'entreprise Kiwilab."
        g"J'ai pu m'améliorer dans plusieurs domaine, et comprendre d'avantage la programmation."

return