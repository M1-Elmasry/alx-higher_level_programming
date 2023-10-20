-- move database `hbtn_0c_0`, table `first_table` and column `name` in `first_table` table to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLAT = utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
