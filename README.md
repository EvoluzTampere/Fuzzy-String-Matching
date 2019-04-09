# Evoluz Project
# First paragraph: general description
Project EVOLUZ, financed by the Academy of Finland (duration: 2017-2021) is a research project, which addresses the need to understand and support historians' work tasks in digital invironment.  Our goal is to understand and to develop methods and tools for improving information interactions of the end users accessing digital cultural heritage collections.  The research is based on the task-based information interactions (TBII paradigm). Personnel: Dr. Heikki Keskustalo (research leader), Dr. Sanna Kumpulainen (user studies), Dr. Boyang Zhang (constructive research and development). National and international cooperation: Dr. Jaap Kamps, University of Amsterdam; Dr. Kimmo Kettunen, National Library of Finland; Dr. Marko Tikka, University of Tampere; Dr. Krisztian NBalog, University of Stavanger; Dr. Thea Lindquist, University of Colorado Boulder.  This GitHub site is intended for documenting and sharing the programming codes developed during the research.
# 
In addition to historians themselves, the digital methods in history research have drawn the attention
of researchers in information studies. Our fields of study include information retrieval and
information behavior. This is an international research effort aiming at supporting digital historians
research work tasks. The context of the research is historian’s research work and we will particularly
focus on (a) research processes and needs descriptions of the historians' work tasks, and (b) the study
the information retrieval in historical document collections, and how to support these with fuzzy
matching methods.
# Second paragraph: research-oriented description: history domain, research problems (goals), data and methods/methodology (TBII viewpoint), NEs
Traditionally, digital access methods in historical research have been studied from the viewpoint of
the document collections and data. Instead of this data-centric view, we adopt information interaction
centered view towards accessing digital collection. Information interaction is understood as
behavioral and cognitive activities related to task planning, searching and selecting information items,
working with information items, and synthetizing and reporting.
Information interaction encompasses searching in the larger task context. This means that the actions
are framed by a motivating task that triggers searching. We aim at better understanding the rationale
behind actions and by this enable combining task-based approach into tool development and
evaluation.
# Third paragraph: keeping track: goals of the project vs the code

# ABOUT (briefly describe of the .py for which purposes, description of the resources).
This repository contains the code to collect .  
The tasks include:
1. collect (one sentence)
2. Language (explain each simple terms with very simple sentences)
3. Identity 
4. Create
5. Perform 

# This cite contains codes for process Finnish historical letters with detailed description

1. dash.py is used to process dash related issues in a meaningful way, dashes appeared in OCRed texts, especially in the end of a line, dash.py is used to handle various situations.
2. stopwords remover.py is used to remove Finnish stopwords, there are the basic stopwords, can be enhanced.
3. snowball.py is the NLTK package of the snowball stemmmer for Finnish languages.
4. 10_selection is used to select everything 10th of the letters, it uses every nth method.
5. BS4historicalExample.py and BeautifulSoup.py are used to analysis semi-structural HTML format historical letters. The package of Beautiful Soup can extract tags <> easy and categorise into various tags, it is a part of the process turnning unstructured raw data to structural database.
6. FiNER install documentation.txt is the instruction on how to install FiNER on your own server, remember to run sudo (superuser).
7. FiNER online.txt is how to download the FiNER.py from the launch server, it helps to test the interface designing. In Kielipankki, the FiNER is running by Lighttpt. 
8. FrequencyCount.py is used to count the word frequency which is similiar to words count, entity frequency, and orderby then groupby with reverse number.
9. Greetings_extraction.py is used to extract a word of the sentence.
10. Linux creat password.txt is used to creat password for users when first launch the CSC cloud.
11. Specific_Element.py is used to extract specific tags of the data with tagging by Beautiful Soup, we can use it to extract one or more tags needed, not all the tags are useful.
12. _init_.py is the NLTK English NER Chunker, the output of the chunker is a nltk.tree object. Named entity recognition example, we can use that as example for annotating Finnish language.
13.nltktest.py is used as example to test snowball stemmer in Finnish language.
14.tokenisation.R is a r-studio programme used to annotating Finnish language, it works well, the limitation is without stemmer.




## Data sources

* [Sotasampo resourse/dataset](http://www.ldf.fi/dataset/warsa)(SPARQL query https://www.w3.org/2009/08/skos-reference/skos.html#)
* [DIGITAALISET AINEISTOT](https://digi.kansalliskirjasto.fi/aikakausi/search)

