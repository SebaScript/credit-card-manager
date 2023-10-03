CREATE TABLE credit_cards (
    card_number VARCHAR( 20 ) NOT NULL,
    owner_id VARCHAR( 20 ) NOT NULL,
    owner_name VARCHAR( 100 ) NOT NULL,
    bank_name VARCHAR( 100 ) NOT NULL,
    due_date DATE NOT NULL,
    franchise VARCHAR( 15 ) NOT NULL,
    payment_day VARCHAR( 2 ) NOT NULL,
    monthly_fee FLOAT,
    interest_rate FLOAT
);