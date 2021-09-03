# AminoAcid Counter

	The goal of this is to count the Nitrogens within any valid amino acid sequence.


The Amino Acid JSON file formats a dictionary in the form
{AcidAbbrv:[int,int,int...]}
Each acid is named by the standard one-letter abbreviations (i.e. G for Glyceine)
The nested list of integer values follow respectively:

Carbon, Hydrogen, Nitrogen, Oxygen, Sulfur


For example:

{"E": "[5,9,1,4]"}
Means there is Carbon(x5), Hydrogen(x9), Nitrogen(x1) and Oxygen(x4)

This is for ease of calculation because I am stupid :)

Valid sequence examples are:

	MNGITIAEINKVIIEPTQKMATAYAEMLVEDLEKMGYKVEKIEREDKIVFKVENKITIITG
---------------
	LAEGEEPRKVSSLRGGEDNVDIKVRVISVEPPKTIHTQRGDRTISEAIVGDETGRVKLTAWGKQAGKLEEGQAVELKGAWTTVYRGQVQLNIGSRGSIEKIEDSEVPKPEDIPETTPKAETAPGQGRGGFRRSYGRRPSGGRRYRPSGEGEEGGEEEGEEGF
