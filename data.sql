-- Populate GasComposition
INSERT INTO diveshopmanagement_gascomposition (gas_type, oxygen_percentage)
VALUES
    ('Air', 21.00),
    ('Enriched Air Nitrox', 32.00),
    ('Trimix', 18.00),
    ('Heliox', 7.00),
    ('Oxygen', 100.00);

-- Populate Tank
INSERT INTO diveshopmanagement_tank (tank_identifier, size, location, hydro_dropoff_date, hydro_pickup_date, hydro_passed)
VALUES
    ('T001', '80 cuft', 'Storage Room A', NULL, NULL, 0),
    ('T002', '100 cuft', 'Storage Room B', NULL, NULL, 0),
    ('T003', '120 cuft', 'Storage Room C', NULL, NULL, 0),
    ('T004', '80 cuft', 'Storage Room A', NULL, NULL, 0),
    ('T005', '100 cuft', 'Storage Room B', NULL, NULL, 0),
    ('T006', '120 cuft', 'Storage Room C', NULL, NULL, 0);

-- Populate Airfill
INSERT INTO diveshopmanagement_airfill (tank_id, fill_pressure, date)
VALUES
    (1, 3000.00, '2023-05-01'),
    (2, 3000.00, '2023-05-01'),
    (3, 3000.00, '2023-05-01'),
    (4, 3000.00, '2023-05-02'),
    (5, 3000.00, '2023-05-02'),
    (6, 3000.00, '2023-05-02');

-- Populate GasBlending
INSERT INTO diveshopmanagement_gasblending (tank_id, gas_composition_id, blending_method, notes)
VALUES
    (1, 1, 'Partial Pressure Mixing', NULL),
    (2, 1, 'Membrane System', NULL),
    (3, 2, 'Partial Pressure Mixing', NULL),
    (4, 2, 'Membrane System', NULL),
    (5, 3, 'Partial Pressure Mixing', NULL),
    (6, 3, 'Membrane System', NULL);

-- Populate HydrostaticTest
INSERT INTO diveshopmanagement_hydrostatictest (tank_id, dropoff_date, pickup_date, result)
VALUES
    (1, '2023-05-10', NULL, 'Pending'),
    (2, '2023-05-10', NULL, 'Pending'),
    (3, '2023-05-10', NULL, 'Pending'),
    (4, '2023-05-11', NULL, 'Pending'),
    (5, '2023-05-11', NULL, 'Pending'),
    (6, '2023-05-11', NULL, 'Pending');

-- Populate TankInventory
INSERT INTO diveshopmanagement_tankinventory (tank_id, status)
VALUES
    (1, 'Available'),
    (2, 'Available'),
    (3, 'Available'),
    (4, 'Available'),
    (5, 'Available'),
    (6, 'Available');

-- Populate User (AbstractUser)
INSERT INTO auth_user (username, password, first_name, last_name, email, is_staff, is_superuser, last_login, date_joined)
VALUES
    ('john', 'pbkdf2_sha256$216000$e7gexwaBXniy$2IHWSUKE8RNBKFqSzE3g9Qj0jux9JKGwKt5l+UuWDF4=', 'John', 'Doe', 'john@example.com', 1, 1, NULL, '2023-05-01'),
    ('jane', 'pbkdf2_sha256$216000$pK39wH8o8GBf$qzFLB0YdOfq8yzQ2RPoBWJw97l7XlffTg9spDhCxP+4=', 'Jane', 'Smith', 'jane@example.com', 1, 0, NULL, '2023-05-02');

-- Populate Organization
INSERT INTO diveshopmanagement_organization (name)
VALUES
    ('ABC Dive Center'),
    ('XYZ Diving School');

-- Populate Certification
INSERT INTO diveshopmanagement_certification (diver_id, certification_level, certification_agency, issue_date, expiration_date)
VALUES
    (1, 'Advanced Open Water Diver', 'PADI', '2020-03-15', '2025-03-15'),
    (2, 'Open Water Diver', 'NAUI', '2021-05-10', '2026-05-10');

-- Populate Customer
INSERT INTO diveshopmanagement_customer (name, birthdate, organization_id, employee, picture, email, phone, address, emergency_contact_name, emergency_contact_phone)
VALUES
    ('John Doe', '1990-01-01', 1, 0, NULL, 'john.doe@example.com', '1234567890', '123 Main St', 'Jane Doe', '0987654321'),
    ('Jane Smith', '1992-05-05', 2, 1, NULL, 'jane.smith@example.com', '9876543210', '456 Oak Ave', 'John Smith', '0123456789');

-- Populate Equipment
INSERT INTO diveshopmanagement_equipment (name, description)
VALUES
    ('BCD', 'Buoyancy Control Device'),
    ('Regulator', 'Scuba Regulator'),
    ('Wetsuit', 'Neoprene Wetsuit'),
    ('Mask', 'Diving Mask'),
    ('Fins', 'Diving Fins');

-- Populate EquipmentInventory
INSERT INTO diveshopmanagement_equipmentinventory (equipment_id, availability, quantity, condition)
VALUES
    (1, 1, 5, 'Good'),
    (2, 1, 5, 'Good'),
    (3, 1, 10, 'Excellent'),
    (4, 1, 10, 'Excellent'),
    (5, 1, 10, 'Good');

-- Populate DiveSite
INSERT INTO diveshopmanagement_divesite (name, description, coordinates, water_conditions)
VALUES
    ('Coral Reef', 'Beautiful coral reef with diverse marine life', '12.3456, -78.9012', 'Clear water, minimal current'),
    ('Cave Dive', 'Underwater cave system for advanced divers', '34.5678, -12.3456', 'Limited visibility, strong current'),
    ('Wreck Dive', 'Sunken shipwreck exploration', '56.7890, -23.4567', 'Moderate visibility, calm water');

-- Populate Course
INSERT INTO diveshopmanagement_course (name)
VALUES
    ('Open Water Diver'),
    ('Advanced Open Water Diver'),
    ('Rescue Diver'),
    ('Divemaster'),
    ('Instructor');

-- Populate Instructor
INSERT INTO diveshopmanagement_instructor (name)
VALUES
    ('Michael Johnson'),
    ('Sarah Thompson');

-- Populate Divemaster
INSERT INTO diveshopmanagement_divemaster (name)
VALUES
    ('Robert Davis'),
    ('Emily Wilson');

-- Populate Dive
INSERT INTO diveshopmanagement_dive (course_id, student_id, phone_number)
VALUES
    (1, 1, '1234567890'),
    (2, 2, '9876543210');

-- Populate DiveContact
INSERT INTO diveshopmanagement_divecontact (dive_id, contact_type, contact_details)
VALUES
    (1, 'Emergency', 'Jane Doe - 0987654321'),
    (2, 'Emergency', 'John Smith - 0123456789');

-- Populate Trip
INSERT INTO diveshopmanagement_trip (name)
VALUES
    ('Cozumel Dive Trip'),
    ('Great Barrier Reef Expedition');

-- Populate StaffSchedule
INSERT INTO diveshopmanagement_staffschedule (staff_id, date, start_time, end_time)
VALUES
    (1, '2023-05-10', '08:00:00', '16:00:00'),
    (2, '2023-05-11', '09:00:00', '17:00:00');

-- Populate DiveLog
INSERT INTO diveshopmanagement_divelog (dive_id, date, duration, depth, location_id)
VALUES
    (1, '2023-05-12', '01:30:00', 18.5, 1),
    (2, '2023-05-13', '01:45:00', 20.2, 2);

-- Populate RentalEquipment
INSERT INTO diveshopmanagement_rentalequipment (dive_id, equipment_id, quantity)
VALUES
    (1, 1, 1),
    (1, 2, 1),
    (2, 3, 1),
    (2, 4, 1);

-- Populate RepairRequest
INSERT INTO diveshopmanagement_repairrequest (equipment_id, description, status)
VALUES
    (1, 'Leaking air bladder', 'Pending'),
    (2, 'Regulator not functioning', 'In Progress');

-- Populate RepairUpdate
INSERT INTO diveshopmanagement_repairupdate (repair_request_id, update_date, update_description)
VALUES
    (1, '2023-05-14', 'Identified damaged O-ring and replaced it.'),
    (2, '2023-05-15', 'Replaced worn-out diaphragm.');

-- Populate Document
INSERT INTO diveshopmanagement_document (name, file)
VALUES
    ('Safety Guidelines', 'safety_guidelines.pdf'),
    ('Equipment Manual', 'equipment_manual.pdf');

-- Populate CourseSchedule
INSERT INTO diveshopmanagement_courseschedule (course_id, start_date, end_date)
VALUES
    (1, '2023-06-01', '2023-06-10'),
    (2, '2023-06-15', '2023-06-20');

-- Populate CourseStudent
INSERT INTO diveshopmanagement_coursestudent (course_schedule_id, student_id, phone_number)
VALUES
    (1, 1, '1234567890'),
    (1, 2, '9876543210');

-- Populate CourseInstructor
INSERT INTO diveshopmanagement_courseinstructor (course_schedule_id, instructor_id)
VALUES
    (1, 1),
    (2, 2);

-- Populate CourseDivemaster
INSERT INTO diveshopmanagement_coursedivemaster (course_schedule_id, divemaster_id)
VALUES
    (1, 1),
    (2, 2);

-- Populate CourseParticipant
INSERT INTO diveshopmanagement_courseparticipant (course_schedule_id, customer_id, phone_number)
VALUES
    (1, 1, '1234567890'),
    (1, 2, '9876543210');
