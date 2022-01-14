CREATE TABLE counties (
    county_id integer NOT NULL,
    county_name varchar(50)
);

DROP TABLE GA_County_Data;
CREATE TABLE IF NOT EXISTS GA_County_Data (
    County_ID INTEGER NOT NULL,
    County_Name VARCHAR(50),
    Per_Capita_Income VARCHAR (20),
    Percent_FRL DECIMAL(4,2),
    Latitude VARCHAR(10),
    Longitude VARCHAR(10),
    PRIMARY KEY(County_ID)
);

DROP TABLE dollar_store_final;
CREATE TABLE dollar_store_final (
    county_name varchar(50) NOT NULL,
    store_name varchar(50),
    store_lat varchar(50),
    store_long varchar(50),
    store_address varchar(50),
	Store_PlaceID varchar(30)
	
);

DROP TABLE fast_food_stores;
CREATE TABLE fast_food_stores (
   
    county_name varchar(50) NOT NULL,
    store_name varchar(50),
    store_lat varchar(50),
    store_long varchar(50),
    store_address varchar(50),
	ff_id varchar(30) NOT NULL
);

-- ALTER TABLE fast_food_stores ALTER COLUMN ff_id ADD GENERATED ALWAYS AS IDENTITY (
--     SEQUENCE NAME fast_food_stores_ff_id_seq
--     START WITH 1
--     INCREMENT BY 1
--     NO MINVALUE
--     NO MAXVALUE
--     CACHE 1
-- );

DROP TABLE ga_counties_schools;
CREATE TABLE ga_counties_schools (
    county_id integer NOT NULL,
	county_name varchar(50), 
    school_id integer,
	School_Name VARCHAR(100),
    percent_frl numeric(4,2),
	address VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    zipcode INTEGER
--     PRIMARY KEY(school_id)
);

DROP TABLE grocery_store; 
CREATE TABLE IF NOT EXISTS grocery_store(
    grocery_store_ID INTEGER NOT NULL,
    County_Name VARCHAR(50),
    Store_Name VARCHAR(50),
    Store_Lat VARCHAR(50),
    Store_Long VARCHAR(50),
    Store_Address VARCHAR(50),
    PRIMARY KEY(grocery_store_ID)
);

ALTER TABLE grocery_store ALTER COLUMN grocery_store_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME grocery_store_grocery_store_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);

DROP TABLE schools_final;
CREATE TABLE schools_final (
	county_id integer NOT NULL,
	county_name varchar(50),
    school_id integer NOT NULL,
    school_name varchar(100),
    percent_frl numeric(4,2),
    address varchar(50),
    city varchar(50),
    state varchar(50),
    zipcode integer,
    latitude varchar(30),
    longitude varchar(30)
);

DROP TABLE stores_final;
CREATE TABLE stores_final (
    school_id integer NOT NULL,
    county_name varchar(50),
    school_name varchar(100),
    school_lat varchar(50),
    school_long varchar(50),
    store_name varchar(50),
    store_lat varchar(50),
    store_long varchar(50),
    store_address varchar(50),
	Store_PlaceID varchar(30)
);

DROP TABLE county_stores_final;
CREATE TABLE IF NOT EXISTS county_stores_final(
    County_Name VARCHAR(50) NOT NULL,
    Per_Capita_Income VARCHAR(20),
    Percent_FRL DECIMAL(4, 2),
    Latitude VARCHAR(50),
    Longitude VARCHAR(50),
    Total_Grocery_Stores DECIMAL,
    Total_Dollar_stores DECIMAL,
    Total_Fast_Food_Places DECIMAL,
    PRIMARY KEY(County_Name)
);

ALTER TABLE ONLY counties
    ADD CONSTRAINT counties_pkey PRIMARY KEY (county_id);

-- ALTER TABLE ONLY dollar_store_final
--     ADD CONSTRAINT dollar_store_final_pkey PRIMARY KEY (Store_PlaceID);
-- removing constraint as store place_ID does not have unique value

-- ALTER TABLE ONLY ga_counties_schools
--     ADD CONSTRAINT ga_counties_schools_pkey PRIMARY KEY (county_id);
-- Primary key constraint added in the create table
	

-- ALTER TABLE ONLY grocery_store
--     ADD CONSTRAINT grocery_store_pkey PRIMARY KEY (grocery_store_id);
-- 	removing constraint as grocery_store_id does not have a unique value

ALTER TABLE ONLY schools_final
    ADD CONSTRAINT schools_final_pkey PRIMARY KEY (school_id);

ALTER TABLE ONLY stores_final
    ADD CONSTRAINT stores_final_pkey PRIMARY KEY (school_id);
