Jeu de strat�gi-�volution
Version 0.5.1

----------------------
Version m�re :
	Jeu stratevol : 0.3.2
	IA : 0.3 
----------------------

But de la version 0.5 :

	1) int�grer l'intelligence artificielle r�seaux de neurones (RN)


----------------------

But de la version 0.5.1 :

	1) pourquoi il font n'importe quoi ?
		- pas de maj des attributs ligne et colonne des ouvriers
		- utilisation du dico

	2) un poids d'une case qui est proche de 0(noir) repousse, proche de 1(blanc) attire
		- modification de poidsCases
		- modification de l'importance du hasard dans IA_Ouvriers


	3) r�solution du bug de bord, lorsque les ia arrive en bord elle tente d'acc�der � des poidsCases inexistant
		-cr�ation du ligne et colonne en plus rempli de 0.99 pour dissuader les ia
			une seule suffisante car indice -1 = indice max

	4) AAAARGH /!\ la cr�ation de la base de donn�e � �chager ligne et colonne
	cad cases[0] =ligne 1 colonne 1 | cases[1] = ligne 2 colonne 1
		- l'id�al serait de modifier la cr�ation de la base de donn�e mais...
		- solution : modification des cases dans la m�thode action de la classe Ouvrier
