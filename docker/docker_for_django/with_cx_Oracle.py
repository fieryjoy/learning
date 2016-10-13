import cx_Oracle


def play():
    connection = cx_Oracle.connect('system/oracle@172.17.0.2/XE')
    print(connection.version)
    cursor = connection.cursor()
    print("list all tables")
    cursor.execute('SELECT owner, table_name FROM dba_tables')
    for result in cursor:
        print(result)

    find_max = '''
        CREATE OR REPLACE FUNCTION findMax(x IN number, y IN number)
        RETURN number
        AS
            z number;
        BEGIN
           IF x > y THEN
              z:= x;
           ELSE
              Z:= y;
           END IF;

           RETURN z;
        END;
        '''
    cursor.execute(find_max)
    numbers = [3, 5]
    result = cursor.callfunc("findMax", cx_Oracle.NUMBER, numbers)
    print("Max between {} is {}".format(numbers, result))
    cursor.close()
    connection.close()