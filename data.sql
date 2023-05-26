-- Populate Certifications
INSERT INTO diveshopmanagement_certification (name)
VALUES
    ('Open Water Diver'),
    ('Advanced Open Water Diver'),
    ('Rescue Diver'),
    ('Divemaster'),
    ('Instructor'),
    ('Master Scuba Diver'),
    ('Assistant Instructor');

-- Populate Organizations
INSERT INTO diveshopmanagement_organization (name)
VALUES
    ('PADI - Professional Association of Diving Instructors'),
    ('NAUI - National Association of Underwater Instructors'),
    ('SSI - Scuba Schools International'),
    ('SDI - Scuba Diving International'),
    ('CMAS - Confédération Mondiale des Activités Subaquatiques'),
    ('BSAC - British Sub-Aqua Club'),
    ('RAID - Rebreather Association of International Divers');

-- Link Certifications with Organizations (example mappings)
INSERT INTO diveshopmanagement_certification_organizations (certification_id, organization_id)
VALUES
    (1, 1),  -- Open Water Diver - PADI
    (2, 1),  -- Advanced Open Water Diver - PADI
    (3, 1),  -- Rescue Diver - PADI
    (4, 1),  -- Divemaster - PADI
    (5, 1),  -- Instructor - PADI
    (6, 1),  -- Master Scuba Diver - PADI
    (7, 1);  -- Assistant Instructor - PADI
