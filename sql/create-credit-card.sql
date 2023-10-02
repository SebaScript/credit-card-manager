CREATE TABLE credit_cards (
    card_number VARCHAR( 20 ) NOT NULL,
    owner_id VARCHAR( 20 ) NOT NULL,
    owner_name TEXT NOT NULL,
    bank_name TEXT NOT NULL,
    due_date DATE,
    franchise TEXT NOT NULL,
    payment_day VARCHAR( 2 ) NOT NULL,
    monthly_fee FLOAT,
    interest_rate FLOAT,
);