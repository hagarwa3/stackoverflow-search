# stackoverflow-search
A system to automatically answer stack overflow / Piazza questions using the stackoverflow data dump + elastic search

Find the entire index of all questions till March 2016 (18GB) at https://goo.gl/aA7q8Q
This is the data indexed by elasticsearch, and while I am not sure about this, I believe that you can directly put this indexed data into the respective elasticsearch folder to have the same setup. I have chosen not to actually host the entire thing because of its huge size.

There are multiple parts to this entire project:
- Parsing the original data (xml files from StackOverflow data dump) and then indexing it into elasticsearch
- Testign multiple different queries to see which gives us the best results
- Building a keyword extraction algorithm for all questions, to do automatic tagging of question
- Integrate all of this in the frontend (HTML+JS+Bootstrap)
