# Development Log
*By Zirui Wang*

## 1. DataBase

**`blog_post_type`**
* id: int NOT NULL PRIMARY KEY AUTOINCREMENT
* type: 

**`blog_post`**
* id: int NOT NULL PRIMARY KEY AUTOINCREMENT
* title: varchar(200) NOT NULL
* \`text\`: text NOT NULL
* created_date: datetime NOT NULL
* published_date: datetime NULL
* author_id: integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
* total_views: integer unsigned NOT NULL CHECK ("total_views" >= 0)

**`blog_mydetail`**
* id: integer NOT NULL PRIMARY KEY AUTOINCREMENT
* name: varchar(50) NOT NULL
* age: varchar(10) NOT NULL
* date_of_birth: date NOT NULL
* phone1: varchar(50) NOT NULL
* phone2: varchar(50) NOT NULL
* email: varchar(50) NOT NULL
* country: varchar(50) NOT NULL
* city: varchar(50) NOT NULL
* address: text NOT NULL
* introduction: text NULL

**`blog_education`**
* id: integer NOT NULL PRIMARY KEY AUTOINCREMENT
* university: varchar(200) NOT NULL UNIQUE
* start_date: date NULL
* end_date: date NULL
* degree: varchar(200) NOT NULL
* college: varchar(200) NOT NULL
* subject: varchar(200) NOT NULL

**`blog_course`**
* id" integer NOT NULL PRIMARY KEY AUTOINCREMENT
* course_name" varchar(100) NOT NULL
* university_id" varchar(200) NOT NULL REFERENCES "blog_education" ("university") DEFERRABLE INITIALLY DEFERRED
* year" smallint unsigned NULL CHECK ("year" >= 0)