# Wellcome to Followers! #

This is a sample of Django project with a single Django application in it.

The project is called "installation" and contains a single application called "followers".
The application counts the number of followers for each man in a social graph, represented by 
"man_man" table of underlying database.

## Requirements ##
 * Django1.7 

Note, that I failed to run it with current Django1.7b4 revision (as of May, 16 2014) due to
what I think is an error in "makemigrations" action - it just refused to see properly
configured application (while being able to perform explicit `import followers` statement). 

Tested with official Django1.7b1 release from https://www.djangoproject.com/download/1.7b1/tarball/.
