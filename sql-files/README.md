

```bash
MariaDB [ragnarok]> describe ragnarok.login
    -> ;
+-----------------+-----------------------+------+-----+---------+----------------+
| Field           | Type                  | Null | Key | Default | Extra          |
+-----------------+-----------------------+------+-----+---------+----------------+
| account_id      | int(11) unsigned      | NO   | PRI | NULL    | auto_increment |
| userid          | varchar(23)           | NO   | MUL |         |                |
| user_pass       | varchar(32)           | NO   |     |         |                |
| sex             | enum('M','F','S')     | NO   |     | M       |                |
| email           | varchar(39)           | NO   |     |         |                |
| group_id        | tinyint(3)            | NO   |     | 0       |                |
| state           | int(11) unsigned      | NO   |     | 0       |                |
| unban_time      | int(11) unsigned      | NO   |     | 0       |                |
| expiration_time | int(11) unsigned      | NO   |     | 0       |                |
| logincount      | mediumint(9) unsigned | NO   |     | 0       |                |
| lastlogin       | datetime              | YES  |     | NULL    |                |
| last_ip         | varchar(100)          | NO   |     |         |                |
| birthdate       | date                  | YES  |     | NULL    |                |
| character_slots | tinyint(3) unsigned   | NO   |     | 0       |                |
| pincode         | varchar(4)            | NO   |     |         |                |
| pincode_change  | int(11) unsigned      | NO   |     | 0       |                |
| vip_time        | int(11) unsigned      | NO   |     | 0       |                |
| old_group       | tinyint(3)            | NO   |     | 0       |                |
+-----------------+-----------------------+------+-----+---------+----------------+
18 rows in set (0.000 sec)

```