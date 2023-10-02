CREATE TABLE payment_plans (
    card_number VARCHAR( 20 ) NOT NULL,
    purchase_date DATE,
    purchase_amount FLOAT,
    payment_date DATE,
    payment_amount FLOAT,
    interest_amount FLOAT,
    capital_amount FLOAT,
    balance FLOAT
);