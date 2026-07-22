--show grantsss
SELECT grantee, privilege_type, table_schema, table_name
FROM information_schema.user_privileges
WHERE grantee IN ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'");