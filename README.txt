# IA-ConcoursM1

Adrien Boitelle
Robin Navarro

Pour notre IA, nous avons utilisé l'algorithme alphaBeta. Au lieux d'utiliser un horizon fixe, nous utilisons un système de jettons.
Pour une meilleure gestion du temps, nous fesons un iterative deepening. Mais au lieux de recalculer tous les coups déjà joués,
en enregistre l'état du jeu quand nous sommes à cours de jettons, pour pouvoir reprendre à cet endroit lors de la prochaine passe s'il 
nous reste du temps. Notre algorithme agit alors plutôt comme un parcours en largeur.

Nous avons une heuristique assez simple qui privilégie les coins et les bords.

Nous utilisons un dictionnaire de coup pour le début de la partie, afin de gagner de temps.
Nous distribuons ensuite le temps restant pour chaque coup, mais avant d'attendre une certaine limite (~30 coups avant la fin),
on diminue le temps alloué pour chaque coup d'environ un tiers.

Nous avons donc plus de temps pour la fin. Comme les tout derniers coups ne demanderont pas beaucoup de temps de calcul,
on prends plus de temps avant la fin, en ajoutant un dizième du temps restant.

Cette gestion du temps nous permet de voir assez tôt la fin de la partie.

Nous avons également essayé d'utilisez le parraléllisme, mais comme nous n'avons qu'un seul coeur lors du concours, nous ne l'utilisons pas.
