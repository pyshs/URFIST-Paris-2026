def calculer_nombre_mots_seuil(phrase, nombre_min_lettres = 4):
    """
    Compter le nombre de mots de plus de N lettres
    """
    sortie_fichier = True 
    liste_mots = phrase.split(" ")
    nombre_mots = len(liste_mots)
    if len(phrase) > 0:
        compteur = 0 
        for i in liste_mots: 
            if len(i) >= nombre_min_lettres: 
                compteur += 1
        proportion = round(100 * compteur / nombre_mots, 2) 
        informations = {
            "Total": compteur,
            "Proportion": proportion,
            "Phrase": phrase,
            "Seuil": nombre_min_lettres,
        }
        return informations
    else:
        return None