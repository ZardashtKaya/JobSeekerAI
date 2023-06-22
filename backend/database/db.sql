create database if not exists jobseekeraidb;
use jobseekeraidb;

create table if not exists employee(
    employee_id int not null auto_increment,
    name varchar(100) not null,
    email varchar(100) not null,
    phone varchar(100) not null,
    primary key(employee_id)
);

create table if not exists skill(
    skill_id int not null auto_increment,
    skill_name varchar(100) not null,
    primary key(skill_id)
);

create table if not exists employee_skill(
    employee_skill_id int not null auto_increment,
    employee_id int not null,
    skill_id int not null,
    primary key(employee_skill_id),
    foreign key(employee_id) references employee(employee_id),
    foreign key(skill_id) references skill(skill_id)
);

create table if not exists rating(
    rating_id int not null auto_increment,
    employee_skill_id int not null,
    rating_percentage decimal(5,2) not null,
    primary key(rating_id),
    foreign key(employee_skill_id) references employee_skill(employee_skill_id)
);
