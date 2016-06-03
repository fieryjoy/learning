USE `BucketList`;
DROP procedure IF EXISTS sp_validateLogin;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_validateLogin`(
IN p_username VARCHAR(100)
)
BEGIN
    select * from tbl_user where user_username = p_username;
END$$
DELIMITER ;