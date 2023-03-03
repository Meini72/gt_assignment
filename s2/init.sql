CREATE TABLE order_table (
    order_id INTEGER PRIMARY KEY,
    item_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    total_item_price numeric NOT NULL,
    total_item_weight numeric NOT null,
    order_date TIMESTAMP not NULL
);


CREATE TABLE item (
    item_id INTEGER PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    manufacturer_name VARCHAR(255) NOT NULL,
    cost numeric NOT NULL,
    weight numeric NOT NULL
);

CREATE TABLE member (
    member_id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    date_of_birth VARCHAR(8) NOT NULL,
    mobile_no VARCHAR(8) NOT NULL
);