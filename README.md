# DbOrmExample

This is a simple script to load an example data file (csv) and write it into a DB. The default config is for sqlite3. 
The intent is to use this to catch bad fields and allow the developer to put in smart validations for the models to 
make sure the data being loaded is valid data. 

## Orator Documentation

is available at [orator-orm.com](https://orator-orm.com/docs/0.9/)

## Installation 

to install orator 
```commandline
> pip install orator
```

then install db backends that you intend to use
```commandline
> pip install psycopg2
> pip install sqlalchemy
```

no need to install sqlite it comes pre-installed with python

## The database

Configuration for the database is done in orator.yml. The example in this repo uses SQLite3 to create a local 
database file. The orator.yml.j2 file is a template that can be populated with the keys for a remote database. 
For the AICS internal modeling database ask me and I'll give you a correctly populated orator.yml file.

## Basics 

Create the table in the database defined in the migrations folder
From the command line: 

```
> orator migrate
```
(answer yes to create the table)

To run the example script to populate the table
```
> python Csv2Db.py 
```

The 'TblGetter.py' file uses orator to pull records from the populated 
database. It also gives simple a simple example of how to query the database
for a subset of data matching a criteria. 
```
> python TblGetter.py
```

'PanadsGetter.py' is an example of using pandas to pull all the data in the 
table into a pandas dataframe. Since the data was checked when the database was 
populated you don't need as much sanity checking in your application.

## File Descriptions

The migrations folder contains the database config files. 
If you're used to working with migrations this can be cool as it
allows you to apply changes to your databases incrementally as well 
as roll back your databases to a prior status. Another useful feature 
is that you can test locally with sqlite3 as a backend before populating 
databases on a production system.

The models folder contains Database table representations (almost no code)

orator.yml is the sqlite has the sqlite database configuration information. 

input_data/ contains an example input csv file. 

