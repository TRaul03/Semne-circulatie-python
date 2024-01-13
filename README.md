Indicații direcție 

(detectare semne circulație cu OpenCV) 

Acest proiect Python utilizează biblioteca OpenCV pentru a realiza detectarea în timp real a cercurilor și analiza culorilor printr-o cameră conectată. Programul captează cadre video, detectează cercuri folosind HoughCircles și analizează culorile dominante în anumite regiuni ale cercurilor detectate. 

 

Contribuții 

Lupu Dan-Mihai - Dominant Color Extraction 

Țaiga Raul-Alexandru - Circle Detection 

Lucru de echipă - Color Analysis 

 

Referințe 

ref.1 - https://docs.opencv.org/4.x/da/d53/tutorial_py_houghcircles.html 

ref.2 - https://www.w3schools.com/python/python_ml_k-means.asp 

Instalare PyCharm - https://www.jetbrains.com/pycharm/download/?section=windows 

Imagini folosite – https://docs.google.com/document/d/1FYLZ-kJ1NDi50Zv1iyFZMkUCDavHJi3P8sK-tBQshww/edit?usp=sharing 

OpenCV - https://opencv.org/ 

Numpy - https://numpy.org/ 

Surse de inspirație - https://chat.openai.com/ ( diverse clarificări + ajutor in ceea ce privește sintaxa) 

 

 

Ex: https://chat.openai.com/share/06dd1f37-c91c-427e-9fa3-2b110af16da8 

      https://chat.openai.com/share/b1b4892d-3580-40d6-9733-001c5d4b243c  

      https://chat.openai.com/share/23bc73d5-802b-483a-9361-c914113ddbdb  

  

https://www.youtube.com/watch?v=kSqxn6zGE0c 

https://www.youtube.com/watch?v=FygLqV15TxQ 

https://pyimagesearch.com/2014/08/04/opencv-python-color-detection/ 

Utilizare 

Asigurați-vă că Python și dependențele necesare sunt instalate. 

• OpenCV: Biblioteca Open Source Computer Vision 

• NumPy: Bibliotecă de calcul științific pentru Python 

PyCharm/Visual Studio sau orice alt compilator 

(Pentru instalarea OpenCV și NumPy vom folosi comanda <pip install opencv-python> respectiv <pip install numpy> sau daca folosiți PyCharm există tutoriale) 

Rulați scriptul accesând fișierul Semne-circulatie.py (RUN) 

Folosind camera de la laptop, vom arata diferite semne circulare care indică direcția (ex. Stop, Mergi in față, Stânga, Dreapta, etc) 

Cum funcționează 

• Programul deschide camera și afișează cadre video. 

• Detectează cercurile folosind algoritmul HoughCircles(vezi ref.1). 

• Pentru fiecare cerc detectat, extrage un pătrat central și determină culoarea dominantă folosind gruparea “k-means”(vezi ref.2). 

• Analiza culorii se realizează în trei zone din pătrat. 

• Logica de decizie bazată pe informațiile de culoare determină acțiuni precum oprirea, virajul la stânga, virajul la dreapta, deplasarea înainte sau N/A (nicio acțiune). 

Backend 

Cele mai importante funcții în care se pot înlocui paramterii: 

-linia 5: get_dominant_color(image,n_colors): parametrul “n_colors” reprezintă numărul de cluster-e(culori dominante) de găsit folosind algoritmul “k-means clustering”. 

-linia 33: onMouse(event,x,y,flags,param): în codul nostru funcția răspunde când “click stânga” este apăsat scurt; event=tipul de acțiune făcută cu mouse-ul; x si y=coordonatele “pointer-ului mouse-ului" cand acțiunea mouse-ului a fost executată; flags=informații adiționale despre acțiune, în codul nostru acest parametru nu este necesar; param=parametri adiționali transmiși funcției recursive, în codul nostru acest parametru nu este necesar. 

-linia 39: cameraCapture = cv2.VideoCapture(0): inițializează camera. În cazul mai multor camere, se schimbă argumentul pentru a opera între ele. 

-linia 56: circles = cv2.HoughCircles(image, method, dp, minDist, param1, param2, minRadius, maxRadius): detectează cercuri într-o imagine folosing “Hough Circle Transform”; image= imaginea introdusă; method=metoda folosită, în OpenCv singura metodă este “cv2.HOUGH_GRADIENT”; dp=rația inversă dintre rezoluția acumulatorului și rezoluția imaginii; minDist=distanța minimă dintre centrele cercurilor detectate; param1=valoarea în gradient folosită pentru detectarea marginilor în “Hough Transform”; param2= pragul de acumulare pentru centrele cercului în stadiul de detectare. Cu cât această valoare este mai mică, cu atât pot fi detectate mai multe cercuri false. Trebuie mărit pentru a reduce pozitive greșite; minRadius=Raza minimă a cercurilor de detectat; maxRadius=Raza maximă a cercurilor de detectat.  

-liniile 76,78: dominant_color[2/0]>x: x reprezintă culoarea pe care o cautăm, în codul nostru 100 este pentru roșu, iar 80 pentru albastru. 

Git 

https://github.com/TRaul03/Semne-circulatie-python/blob/main/Semne-circulatie.py 

 
