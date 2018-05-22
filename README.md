# DbOrmExample

This is a simple script to load an example data file (csv) and write it into a DB. The default config is for sqlite3. The intent is to use this to catch bad fields and allow the developer to put in smart validations for the models to make sure the data being loaded is valid data. 

## Basics 

From the command line: 

```
> orator migrate
```
(answer yes to create the database)
```
> python Csv2Db.py 
```

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

