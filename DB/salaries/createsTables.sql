create table temp_data
(
    job_title varchar(255),
    salary_amount real,
    salary_currency varchar(3),
    conversion_ratio double precision,
    country varchar(255),
    city varchar(255),
    state varchar(255),
    reference_year integer,
    remote_ratio real,
    company_industry varchar(255),
    company_size varchar(1),
    education varchar(255),
    experience_level varchar(2),
    employment_type varchar(2)
);

CREATE TABLE country
(
    key_c serial primary key,
    country varchar(255) NOT NULL,
    city varchar(255),
    state varchar (255)
);

insert into country
    (country, city, state)
select distinct country, city, state
from temp_data

CREATE TABLE job
(
    key_jt serial primary key,
    job_title varchar(255) NOT NULL,
    remote_ratio real,
    experience_level varchar(2),
    employment_type varchar(2),
    education varchar(255)
);

insert into job
    (job_title, remote_ratio, experience_level, employment_type, education)
select distinct job_title, remote_ratio, experience_level, employment_type, education
from temp_data

CREATE TABLE currency
(
    key_cu serial primary key,
    currency varchar(3) NOT NULL,
    conversion_ratio double precision NOT NULL
);
insert into currency
    (currency, conversion_ratio)
select distinct salary_currency, conversion_ratio
from temp_data

CREATE TABLE year
(
    key_ry serial primary key,
    year integer
);
insert into year
    (year)
select distinct reference_year
from temp_data

CREATE TABLE company
(
    key_ci serial primary key,
    company_industry varchar(255),
    company_size varchar(1)
);

insert into company
    (company_industry, company_size)
select distinct company_industry, company_size
from temp_data

create table salary
(
    salary_id serial,
    key_c integer,
    key_jt integer,
    key_ci integer,
    key_ry integer,
    key_cu integer,
    amount real,
    foreign key (key_c) references country(key_c),
    foreign key (key_jt) references job(key_jt),
    foreign key (key_ci) references company(key_ci),
    foreign key (key_ry) references year(key_ry),
    foreign key (key_cu) references currency(key_cu),
    primary key (salary_id, key_c, key_jt, key_ci, key_ry, key_cu)
);

INSERT INTO salary
    (key_c, key_jt, key_ci, key_ry, key_cu, amount)
SELECT
    (SELECT key_c
    FROM country
    WHERE COALESCE(country, 'unknown') = COALESCE(temp_data.country, 'unknown')
        AND COALESCE(city, 'unknown') = COALESCE(temp_data.city, 'unknown')
        AND COALESCE(state, 'unknown') = COALESCE(temp_data.state, 'unknown')),

    (SELECT key_jt
    FROM job
    WHERE COALESCE(job_title, 'unknown') = COALESCE(temp_data.job_title, 'unknown')
        AND COALESCE(remote_ratio, -1) = COALESCE(temp_data.remote_ratio, -1)
        AND COALESCE(experience_level, 'unknown') = COALESCE(temp_data.experience_level, 'unknown')
        AND COALESCE(employment_type, 'unknown') = COALESCE(temp_data.employment_type, 'unknown')
        AND COALESCE(education, 'unknown') = COALESCE(temp_data.education, 'unknown')),

    (SELECT key_ci
    FROM company
    WHERE COALESCE(company_industry, 'unknown') = COALESCE(temp_data.company_industry, 'unknown')
        AND COALESCE(company_size, 'unknown') = COALESCE(temp_data.company_size, 'unknown')),

    (SELECT key_ry
    FROM year
    WHERE COALESCE(year, -1) = COALESCE(temp_data.reference_year, -1)),

    (SELECT key_cu
    FROM currency
    WHERE COALESCE(currency, 'unknown') = COALESCE(temp_data.salary_currency, 'unknown')
        AND COALESCE(conversion_ratio, -1) = COALESCE(temp_data.conversion_ratio, -1)),

    temp_data.salary_amount
FROM temp_data;