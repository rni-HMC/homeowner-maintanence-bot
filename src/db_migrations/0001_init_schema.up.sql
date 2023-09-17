CREATE TABLE `tasks` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255),
  `seconds_between_completions` integer,
  `cost` integer,
  `type_id` integer,
  `area_id` integer
);

CREATE TABLE `types` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL
);

CREATE TABLE `areas` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL
);

CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL
);

CREATE TABLE `attempts` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `task_id` integer NOT NULL,
  `title` varchar(255),
  `notes` varchar(255),
  `user_id` integer NOT NULL,
  `status` varchar(255),
  `created_at` timestamp,
  `completed_at` timestamp,
  `cost` integer
);

CREATE INDEX `attempts_index_0` ON `attempts` (`user_id`);

CREATE INDEX `attempts_index_1` ON `attempts` (`user_id`, `task_id`);

ALTER TABLE `types` COMMENT = 'Cleaning, inspection/repair, etc.';

ALTER TABLE `areas` COMMENT = 'Plumbing, Appliances, etc.';

-- Can't use foreign keys in PlanetScale

-- ALTER TABLE `tasks` ADD FOREIGN KEY (`type_id`) REFERENCES `types` (`id`)

-- ALTER TABLE `tasks` ADD FOREIGN KEY (`area_id`) REFERENCES `areas` (`id`)

-- ALTER TABLE `attempts` ADD FOREIGN KEY (`task_id`) REFERENCES `tasks` (`id`)

-- ALTER TABLE `attempts` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
