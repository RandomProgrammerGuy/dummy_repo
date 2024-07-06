-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `orders` (
    `row_id` int  NOT NULL ,
    `order_id` varchar(10)  NOT NULL ,
    `created_at` datetime  NOT NULL ,
    `item_id` int  NOT NULL ,
    `quantity` int  NOT NULL ,
    `customer_id` int  NOT NULL ,
    `delivery` boolean  NOT NULL ,
    `delivery_key` int  NOT NULL ,
    PRIMARY KEY (
        `row_id`
    )
);

CREATE TABLE `customers` (
    `customer_id` int  NOT NULL ,
    `customer_fname` varchar(50)  NOT NULL ,
    `customer_lname` varchar(50)  NOT NULL ,
    PRIMARY KEY (
        `customer_id`
    )
);

CREATE TABLE `delivery_adds` (
    `delivery_key` int  NOT NULL ,
    `delivery_add` varchar(200)  NOT NULL ,
    `delivery_zip` int  NOT NULL ,
    `delivery_cty` varchar(200)  NOT NULL ,
    PRIMARY KEY (
        `delivery_key`
    )
);

CREATE TABLE `items` (
    `item_id` int  NOT NULL ,
    `sku` varchar(50)  NOT NULL ,
    `item_name` varchar(50)  NOT NULL ,
    `item_category` varchar(50)  NOT NULL ,
    `item_size` varchar(20)  NOT NULL ,
    `item_price` decimal(5,2)  NOT NULL ,
    PRIMARY KEY (
        `item_id`
    )
);

CREATE TABLE `ingredients` (
    `ing_id` varchar(10)  NOT NULL ,
    `ing_name` varchar(50)  NOT NULL ,
    `ing_weight` int  NOT NULL ,
    `ing_meas` varchar(50)  NOT NULL ,
    `ing_price` decimal(5,2)  NOT NULL ,
    PRIMARY KEY (
        `ing_id`
    )
);

CREATE TABLE `recipes` (
    `row_id` int  NOT NULL ,
    `recipe_id` varchar(10)  NOT NULL ,
    `ing_id` varchar(10)  NOT NULL ,
    `qty` int  NOT NULL ,
    PRIMARY KEY (
        `row_id`
    )
);

CREATE TABLE `inventory` (
    `inv_id` int  NOT NULL ,
    `item_id` varchar(10)  NOT NULL ,
    `qty` int  NOT NULL ,
    PRIMARY KEY (
        `inv_id`
    )
);

CREATE TABLE `staff` (
    `staff_id` int  NOT NULL ,
    `staff_fname` varchar(20)  NOT NULL ,
    `staff_lname` varchar(20)  NOT NULL ,
    `staff_pos` varchar(20)  NOT NULL ,
    `staff_salary` decimal(5,2)  NOT NULL ,
    PRIMARY KEY (
        `staff_id`
    )
);

CREATE TABLE `shifts` (
    `shift_id` varchar(10)  NOT NULL ,
    `day` varchar(10)  NOT NULL ,
    `start` datetime  NOT NULL ,
    `end` datetime  NOT NULL ,
    PRIMARY KEY (
        `shift_id`
    )
);

CREATE TABLE `rota` (
    `row_id` int  NOT NULL ,
    `rota_id` varchar(10)  NOT NULL ,
    `date` datetime  NOT NULL ,
    `shift_id` varchar(10)  NOT NULL ,
    `staff_id` int  NOT NULL ,
    PRIMARY KEY (
        `row_id`
    )
);

ALTER TABLE `orders` ADD CONSTRAINT `fk_orders_item_id` FOREIGN KEY(`item_id`)
REFERENCES `items` (`item_id`);

ALTER TABLE `customers` ADD CONSTRAINT `fk_customers_customer_id` FOREIGN KEY(`customer_id`)
REFERENCES `orders` (`customer_id`);

ALTER TABLE `delivery_adds` ADD CONSTRAINT `fk_delivery_adds_delivery_key` FOREIGN KEY(`delivery_key`)
REFERENCES `orders` (`delivery_key`);

ALTER TABLE `recipes` ADD CONSTRAINT `fk_recipes_recipe_id` FOREIGN KEY(`recipe_id`)
REFERENCES `items` (`sku`);

ALTER TABLE `recipes` ADD CONSTRAINT `fk_recipes_ing_id` FOREIGN KEY(`ing_id`)
REFERENCES `ingredients` (`ing_id`);

ALTER TABLE `inventory` ADD CONSTRAINT `fk_inventory_inv_id` FOREIGN KEY(`inv_id`)
REFERENCES `ingredients` (`ing_id`);

ALTER TABLE `shifts` ADD CONSTRAINT `fk_shifts_shift_id` FOREIGN KEY(`shift_id`)
REFERENCES `rota` (`shift_id`);

ALTER TABLE `rota` ADD CONSTRAINT `fk_rota_date` FOREIGN KEY(`date`)
REFERENCES `orders` (`created_at`);

ALTER TABLE `rota` ADD CONSTRAINT `fk_rota_staff_id` FOREIGN KEY(`staff_id`)
REFERENCES `staff` (`staff_id`);

