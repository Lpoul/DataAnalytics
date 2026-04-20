USE lana_dog_walking;

INSERT INTO Financial_Information
(Payment_ID, Payment_Amount, Payment_Method, Payment_Status, Outstanding_Balance) VALUES
(1, 32.00, 'Card', 'Paid', 0.00),
(2, 28.00, 'Cash', 'Paid', 0.00),
(3, 40.00, 'Card', 'Unpaid', 40.00),
(4, 24.00, 'Card', 'Paid', 0.00),
(5, 36.00, 'Card', 'Paid', 0.00),
(6, 30.00, 'Cash', 'Unpaid', 30.00),
(7, 28.00, 'Card', 'Paid', 0.00),
(8, 32.00, 'Card', 'Paid', 0.00),
(9, 26.00, 'Cash', 'Paid', 0.00),
(10, 40.00, 'Card', 'Unpaid', 40.00),
(11, 28.00, 'Card', 'Paid', 0.00),
(12, 35.00, 'Card', 'Paid', 0.00),
(13, 30.00, 'Cash', 'Paid', 0.00),
(14, 42.00, 'Card', 'Unpaid', 42.00),
(15, 26.00, 'Card', 'Paid', 0.00);

INSERT INTO Client_Information
(Client_ID, Name, Phone_Number, Email, Address, Payment_ID) VALUES
(1, 'Jack Morrison', '267-555-1023', 'jack.morrison@example.com', '12 Oak Ridge Ln, Willow Grove, PA', 1),
(2, 'Lana Peters', '215-555-8891', 'lana.peters@example.com', '88 Crestview Dr, Abington, PA', 2),
(3, 'Marcus Hill', '267-555-7712', 'marcus.hill@example.com', '402 Maple Ave, Horsham, PA', 3),
(4, 'Tina Alvarez', '215-555-3344', 'tina.alvarez@example.com', '19 Brookside Rd, Hatboro, PA', 4),
(5, 'Robert Chen', '267-555-9001', 'robert.chen@example.com', '55 Meadowbrook Ln, Jenkintown, PA', 5),
(6, 'Samantha Price', '215-555-1209', 'samantha.price@example.com', '101 Evergreen St, Willow Grove, PA', 6),
(7, 'Daniel Foster', '267-555-4432', 'daniel.foster@example.com', '77 Pine Hill Rd, Abington, PA', 7),
(8, 'Olivia Bennett', '215-555-6678', 'olivia.bennett@example.com', '230 Cedar Ave, Horsham, PA', 8),
(9, 'Henry Lawson', '267-555-9981', 'henry.lawson@example.com', '14 Ridgewood Ct, Hatboro, PA', 9),
(10, 'Grace Turner', '215-555-2210', 'grace.turner@example.com', '300 Willow Ave, Willow Grove, PA', 10),
(11, 'Ethan Brooks', '267-555-7654', 'ethan.brooks@example.com', '92 Highland Rd, Abington, PA', 11),
(12, 'Maya Singh', '215-555-8765', 'maya.singh@example.com', '18 Orchard Ln, Horsham, PA', 12),
(13, 'Jason Carter', '267-555-3345', 'jason.carter@example.com', '66 Forest Dr, Hatboro, PA', 13),
(14, 'Ava Ramirez', '215-555-9087', 'ava.ramirez@example.com', '120 Birchwood Rd, Jenkintown, PA', 14),
(15, 'Logan Wright', '267-555-5566', 'logan.wright@example.com', '41 Elmwood Ave, Willow Grove, PA', 15);

INSERT INTO Dog_Information
(Dog_ID, Name, Breed, Age, Client_ID) VALUES
(1, 'Buddy', 'Beagle', 4, 1),
(2, 'Max', 'Labrador', 3, 2),
(3, 'Bella', 'Poodle', 2, 3),
(4, 'Rocky', 'Bulldog', 5, 4),
(5, 'Luna', 'Husky', 1, 5),
(6, 'Charlie', 'Terrier', 6, 6),
(7, 'Milo', 'Corgi', 4, 7),
(8, 'Daisy', 'Golden Retriever', 3, 8),
(9, 'Cooper', 'Boxer', 2, 9),
(10, 'Sadie', 'Beagle', 7, 10),
(11, 'Bailey', 'Labrador', 3, 11),
(12, 'Chloe', 'Poodle', 2, 12),
(13, 'Zeus', 'German Shepherd', 5, 13),
(14, 'Ruby', 'Husky', 1, 14),
(15, 'Finn', 'Terrier', 4, 15);

INSERT INTO Walk_Information
(Walk_ID, Date, Walker_Name, Bathroom_Activity, Dog_ID) VALUES
(1, '2026-04-01', 'Lana', 'Both', 1),
(2, '2026-04-01', 'Jack', 'Pee', 2),
(3, '2026-04-02', 'Marcus', 'Both', 3),
(4, '2026-04-02', 'Tina', 'Pee', 4),
(5, '2026-04-03', 'Robert', 'Both', 5),
(6, '2026-04-03', 'Samantha', 'Pee', 6),
(7, '2026-04-04', 'Daniel', 'Both', 7),
(8, '2026-04-04', 'Olivia', 'Pee', 8),
(9, '2026-04-05', 'Henry', 'Both', 9),
(10, '2026-04-05', 'Grace', 'Pee', 10),
(11, '2026-04-06', 'Ethan', 'Both', 11),
(12, '2026-04-06', 'Maya', 'Pee', 12),
(13, '2026-04-07', 'Jason', 'Both', 13),
(14, '2026-04-07', 'Ava', 'Pee', 14),
(15, '2026-04-08', 'Logan', 'Both', 15);

