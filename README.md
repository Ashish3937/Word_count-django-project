# Word_count-django-project

This is a basic Django project which can be used to count and extract the most occuring words in a given text file.
The following are the dependecies you will need for the project.Install them using pip in your python environment.


Django2.0.5
nltk


The "logic.py" file contains the method "show()" which is called to derive the result.I have used "nltk.stopwords" to remove frequently occuring words such as 'The','What','If' etc.
"nltk.word_tokenize" is used to convert the entire file into a list of words.
Then a python dictionary was used to store the words according to their number of occurences.

Once you have downloaded the project go inside the project directory and run the following command "python manage.py runserver" and copy the generated link in the browser.


In the logic file:
I have also appended the stop words with additional words and special characters.
