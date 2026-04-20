DROP SCHEMA IF EXISTS lana_dog_walking;
CREATE SCHEMA lana_dog_walking;
USE lana_dog_walking;
-- ============================================
-- 1. FINANCIAL INFORMATION (must be created first)
-- ============================================
CREATE TABLE Financial_Information (
    Payment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Payment_Amount DECIMAL(10,2),
    Payment_Method VARCHAR(50),
    Payment_Status VARCHAR(50),
    Outstanding_Balance DECIMAL(10,2)
);

-- ============================================
-- 2. CLIENT INFORMATION
-- ============================================
CREATE TABLE Client_Information (
    Client_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Phone_Number VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255),
    Payment_ID INT,   -- FK to Financial Information
    FOREIGN KEY (Payment_ID) REFERENCES Financial_Information(Payment_ID)
);

-- ============================================
-- 3. DOG INFORMATION
-- ============================================
CREATE TABLE Dog_Information (
    Dog_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Breed VARCHAR(100),
    Age INT,
    Client_ID INT NOT NULL,
    FOREIGN KEY (Client_ID) REFERENCES Client_Information(Client_ID)
);

-- ============================================
-- 4. WALK INFORMATION
-- ============================================
CREATE TABLE Walk_Information (
    Walk_ID INT AUTO_INCREMENT PRIMARY KEY,
    Date DATE NOT NULL,
    Walker_Name VARCHAR(100),
    Bathroom_Activity VARCHAR(255),
    Dog_ID INT NOT NULL,
    FOREIGN KEY (Dog_ID) REFERENCES Dog_Information(Dog_ID)
);


