CREATE TABLE brand(
  name VARCHAR(100) PRIMARY KEY,
  id SERIAL,
  abreviation VARCHAR(10)
);

CREATE TABLE product(
  production_time INT,
  name VARCHAR(100),
  brand VARCHAR(100) REFERENCES brand(name),
  unit VARCHAR(10),
  type VARCHAR(30),
  description VARCHAR(255),
  code VARCHAR(30) PRIMARY KEY,
  id SERIAL,
  current_selling_price INT,
  current_quantity INT,
  image TEXT
);

CREATE TABLE production_needs(
  product_out VARCHAR(30) REFERENCES product(code),
  product_in VARCHAR(30) REFERENCES product(code),
  quantity INT,
  PRIMARY KEY (product_out, product_in)
);

CREATE TABLE purchase(
  product VARCHAR(30) REFERENCES product(code),
  quantity INT,
  price INT,
  entity VARCHAR(255),
  action_date INT
);

CREATE TABLE sale(
  product VARCHAR(30) REFERENCES product(code),
  quantity INT,
  price INT,
  entity VARCHAR(255),
  action_date INT
);

CREATE TABLE produce(
  product VARCHAR(30) REFERENCES product(code),
  quantity INT,
  action_date INT
);