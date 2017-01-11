# CSV django parser

Application objectives:

1. Fork that repository.

2. In your fork create following steps

3. Create django project `./manage.py startproject csvparser`

4. Create django application named parser `./manage.py startapp parser`

5. Create parser app with view under url of `/parser/upload` 
   * for GET 
      * return html with a form which would let user upload a csv file
   * for POST 
      * parse uploaded csv file with proper handling of exceptions. Sample file is part of this project ().
      * save data into database
  
6. Create list view under `/parser/list` display output of parsed csv in table.

7. Submit Pull request towards `https://github.com/limebrains/csv-django-parser`

## We highly recommend usage of [celery](http://docs.celeryproject.org/en/latest/) for asynchronous parsing.
