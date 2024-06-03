# Facial Expression Analyzer Website Library

![Flask and DashAndData Logo](https://venturer.dashanddata.com/website_assets_images/dd_and_flask_02-400x209.png)

## Description
This is an application that takes pictures of users and sends them to Google Vision for facial expression analysis.
This library includes the fea_config and the fea_models packages. 
- fea_config contains the all the environmental varaibles
- fea_models contains the MySQL database schema and other database related objects.


## Documentation
This uses MySQL and in order to create the tables you must do it from a terminal:
```
from sqlalchemy import create_engine
from fea_models import Base,engine
from fea_config import ConfigWorkstation
config = ConfigWorkstation()
new_engine_str = f"mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_SERVER}/{config.MYSQL_DATABASE_NAME}"
new_engine = create_engine(new_engine_str)
Base.metadata.create_all(new_engine)
```

## Project Folder Structure 

```
.
├── project_resources
│   ├── assets
│   │   ├── favicons
│   │   └── images
│   ├── blog
│   │   └── posts
│   ├── logs
│   └── media
└──  databases
       ├── database.db
       └── db_uploads
```

## Create database
```
create database facial_expression_analyzer;
CREATE USER 'fea_user_00'@'localhost' IDENTIFIED BY 'let_me_in';
GRANT ALL PRIVILEGES ON facial_expression_analyzer.* TO 'fea_user_00'@'localhost';
```
