# simple-portfolio
My portfolio made using [Django](https://github.com/django/django) framework

## Installation

1. Create a Python 3.8 virtualenv and activate it

2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Create tables
    ```sh
    manage.py makemigrations
    manage.py migrate
    ```

4. Collect static files
    ```sh
    manage.py collectstatic
    ```
    
5. Run server
    ```sh
    manage.py runserver
    ```

## Contact
Pedro Horchulhack - pedro.horchulhack@pucpr.edu.br

## Contributing
1. Fork the repository
2. Create a feature branch (```git checkout -b feature_fooBar```)
3. Commit your changes (```git commit -am "Added feature"```)
4. Push your previously created branch (```git push origin feature_fooBar```)
5. Create a pull request
