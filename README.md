Indicații direcție
(detectare semne circulație cu OpenCV)



Acest proiect Python utilizează biblioteca OpenCV pentru a realiza detectarea în timp real a cercurilor și analiza culorilor printr-o cameră conectată. Programul captează cadre video, detectează cercuri folosind HoughCircles și analizează culorile dominante în anumite regiuni ale cercurilor detectate.

Contribuții
Țaiga Raul-Alexandru-
Lupu Dan-Mihai-


Referințe
ref.1 - https://docs.opencv.org/4.x/da/d53/tutorial_py_houghcircles.html
ref.2 - https://www.w3schools.com/python/python_ml_k-means.asp
Instalare PyCharm - https://www.jetbrains.com/pycharm/download/?section=windows
Imagini folosite – 
OpenCV - https://opencv.org/
Numpy - https://numpy.org/
Surse de inspirație - https://chat.openai.com/ ( diverse clarificări + ajutor in ceea ce privește sintaxa)
Ex: https://chat.openai.com/share/06dd1f37-c91c-427e-9fa3-2b110af16da8
-	https://www.youtube.com/watch?v=kSqxn6zGE0c
-	https://www.youtube.com/watch?v=FygLqV15TxQ


Utilizare
1.	Asigurați-vă că Python și dependențele necesare sunt instalate.
• OpenCV: Biblioteca Open Source Computer Vision
• NumPy: Bibliotecă de calcul științific pentru Python
•	PyCharm/Visual Studio sau orice alt compilator
(Pentru instalarea OpenCV și NumPy vom folosi comanda <pip install opencv-python> respectiv <pip install numpy> sau daca folosiți PyCharm există tutoriale)
2.	Rulați scriptul accesând fișierul Semne-circulatie.py (RUN)
3.	Folosind camera de la laptop, vom arata diferite semne circulare care indică direcția (ex. Stop, Mergi in față, Stânga, Dreapta, etc)


Cum funcționează
• Programul deschide camera și afișează cadre video.
• Detectează cercurile folosind algoritmul HoughCircles(vezi ref.1).
• Pentru fiecare cerc detectat, extrage un pătrat central și determină culoarea dominantă folosind gruparea “k-means”(vezi ref.2).
• Analiza culorii se realizează în trei zone din pătrat.
• Logica de decizie bazată pe informațiile de culoare determină acțiuni precum oprirea, virajul la stânga, virajul la dreapta, deplasarea înainte sau N/A (nicio acțiune).
