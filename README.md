# Python CLI Contacts Application
A simple Contact Book made with Python, Postgres, and vObject


## Description:
This Contact book has full CRUD (Create, Read, Update, Delete) capability along with vCard export support, to send contact files to your smartphone. Users can also search by first name, last name, database id, or number with full support for partial matches. 

## Technologies
- Python3
- PostgreSQL
- PeeWee
- pyscopg2
- [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)
- [vObject](https://github.com/eventable/vobject)
- regex

## Installation
1. Clone down the repository and `cd` into the `lib`  directory

    ```
    git clone github.com/daniel-edminster/python-contacts && cd python-contacts/lib
    ```

2. Install dependencies

    ```
    pipenv install peewee psycopg2 autopep8 phonenumbers vobject
    ```

3. Create & seed our contacts database

    ```
    psql < seed.sql
    ```

3. Initialize our virtual environment

    ```
    pipenv shell
    ```

4. Start the application

    ```
    python3 contact.class.py
    ```

## Usage
```
=======Contact Manager=======
| 1: Add New Contact        |
| 2: Update a Contact       |
| 3: Delete a Contact       |
| 4: List all Contacts      |
| 5: Search for Contacts    |
| 6: Export contacts as VCF |
| 7: Exit this program      |
=============================
```

Pretty self-explanatory. 

`1. Add a new Contact` prompts for a first name, last name, and 10 digit phone number. Any tomfoolery is regex’d out by default, number format is 10 digit US for now.

`2. Update existing Contact` prompts for a contact search (ID, first name, last name, or number), will provide you a list of matches and allow you to edit the properties of a contact by providing its ID. 

`3. Delete a Contact` allows deletion of contact by supplying its ID.

`4. List all Contacts` prints every contact in the database to the command line, chronologically.

`5. Search for Contacts` prompts for a contact search (ID, first name, last name, or number), will provide you a list of matches. 

`6. Export Contacts as VCF` will export every contact in the database as a valid, VCF 3.0 file with the naming convention: `id-first_name-last_name.vcf` in the `lib` directory.

`7. Exit this Program` Deletes your system32 and crashes python. But really just exits the program.

## Contribute

- Source: https://github.com/daniel-edminster/python-contacts
- Issue Tracker: https://github.com/daniel-edminster/python-contacts/issues


