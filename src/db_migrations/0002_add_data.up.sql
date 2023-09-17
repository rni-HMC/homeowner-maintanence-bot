INSERT INTO tasks
VALUES (1, 'Clean clothes washer filter', 'Turn off the washer. Locate the filter lid near the bottom right/left. Place a towel on the ground, under the lid. Place a sheet pan over the towel. Open the lid. Remove the drain tube. Drain into sheet pan. Remove the filter by turning it - it should be threaded in. Clean the filter by hand thoroughly. Screw it back in. Cap the drain line and place back in. Close the lid.', 2592000, 0, 1, 1);

INSERT INTO tasks
VALUES (2, 'Clean dishwasher screen', 'Locate and remove the dishwasher filter. Clean. Replace.', 3888000, 0, 1, 1);

INSERT INTO tasks
VALUES (3, 'Exercise Angle Stops', 'Turn off the water to the house. Turn on all the faucets in the house. Turn off the angle stops. Turn the water back on. Turn the angle stops back on.', 5184000, 0, 2, 2);

INSERT INTO types
VALUES (1, 'Cleaning');

INSERT INTO types
VALUES (2, 'Inspection / Repair');

INSERT INTO areas
VALUES (1, 'Appliances');

INSERT INTO areas
VALUES (2, 'Plumbing');

INSERT INTO users
VALUES (1, 'test_user', '2020-01-01 00:00:00');

INSERT INTO attempts
VALUES (1, 1, 'Clean clothes washer filter', 'Cleaned the filter. It was gross.', 1, 'completed', '2020-01-01 00:00:00', '2020-01-01 00:00:00', 0);
