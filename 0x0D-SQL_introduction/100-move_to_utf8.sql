-- convert database,table and field to UTF8
SET NAMES utf8;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE first_name MODIFY name SET utf8 COLLATE utf8_unicode_ci;
