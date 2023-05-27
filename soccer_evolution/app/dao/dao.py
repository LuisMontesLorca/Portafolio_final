# IMPORT TRACE ERROR 
import traceback

# LIBRARY FOR SIMPLE PRIMARY KEY

def statement_select_all(table_name, columns_name):
    return 'SELECT {0} FROM {1}'.format(', '.join(columns_name), table_name)

def statement_select_by_id(table_name, columns_name):
    return 'SELECT {0} FROM {1} WHERE {2} = %s'.format(', '.join(columns_name), table_name, columns_name[0])

def statement_insert_autoincrement_id(table_name, columns_name):
    return 'INSERT INTO {0} ({1}) VALUES ({2})'.format(table_name, ', '.join(columns_name[1:]), ', '.join('%s' for item in columns_name[1:]))

def statement_update_by_id(table_name, columns_name):
    return 'UPDATE {0} SET {1} WHERE {2} = %s'.format(table_name, ', '.join('{0} = %s'.format(item) for item in columns_name[1:]), columns_name[0])

def statement_delete_by_id(table_name, columns_name):
    return 'DELETE FROM {0} WHERE {1} = %s'.format(table_name, columns_name[0])

def dao_generic(app, mysql, table, columns):

    def select_all():
        cursor = None
        try:
            # CREATING CONNECTION CURSOR
            cursor = mysql.connection.cursor()
            # EXECUTE SELECT ALL
            SELECT_ALL = statement_select_all(table, columns)
            if app.debug :  
                print('SELECT_ALL: ', SELECT_ALL)
            cursor.execute(SELECT_ALL, ())
            # GET ROWS
            rows = cursor.fetchall()
            items=[]
            # CREATE ARRAY TO DICTIONARY
            for row in rows:
                # CREATE DICTIONARY
                item = dict(zip(columns, row))
                # ADD ITEM TO ARRAY
                items.append(item)
            # CLOSE CURSOR
            cursor.close()
            if app.debug :    
                print('items:' , items)
            # RETURN ARRAY        
            return items
        except Exception as e:
            if cursor is not None:
                # CLOSE CURSOR
                cursor.close()
            # PRINT ERROR
            traceback.print_exc()
            raise e

    def insert(data):
        cursor = None
        new_data = {}
        try:
            # CREATING CONNECTION CURSOR
            cursor = mysql.connection.cursor()
            # EXECUTE INSERT  
            INSERT = statement_insert_autoincrement_id(table,  columns)
            if app.debug :    
                print('DATA: ', data)
                print('INSERT: ', INSERT)
                print('VALUES:' , list(data.values()))
            cursor.execute(INSERT, list(data.values()))
            # GET AUTOINCREMENT ID
            id = cursor.lastrowid
            new_data[columns[0]] = id
            new_data.update(data)
            # COMMIT TRANSACTION
            mysql.connection.commit()
            # CLOSE CURSOR
            cursor.close()        
            print('id:' , id)
            # CREATE AND RETURN DICTIONARY
            return new_data
        except Exception as e:
            if cursor is not None:
                # CLOSE CURSOR
                cursor.close()
            # PRINT ERROR
            traceback.print_exc()
            raise e

    def update(data):
        cursor = None
        try:
            # CREATING CONNECTION CURSOR
            cursor = mysql.connection.cursor()
            UPDATE = statement_update_by_id(table, columns)
            update_data = list(data.values())[1:]
            update_data.append(list(data.values())[0])
            if app.debug :    
                print('DATA: ', data)
                print('UPDATE: ', UPDATE)
                print('VALUES:' , update_data)
            # EXECUTE INSERT
            cursor.execute(UPDATE, update_data)
            # COMMIT TRANSACTION
            mysql.connection.commit()
            # CLOSE CURSOR
            cursor.close()        
            # CREATE AND RETURN DICTIONARY
            return data
        except Exception as e:
            if cursor is not None:
                # CLOSE CURSOR
                cursor.close()
            # PRINT ERROR
            traceback.print_exc()
            raise e

    def select_by_id(id):
        cursor = None
        try:
            # CREATING CONNECTION CURSOR
            cursor = mysql.connection.cursor()
            # EXECUTE SELECT BY ID
            cursor.execute(statement_select_by_id(table, columns), (id,))
            # GET ROW
            row = cursor.fetchone()
            if row is None :
                # CLOSE CURSOR
                cursor.close()             
                return None
            else :
            # CREATE DICTIONARY            
                item = dict(zip(columns, row))
                # CLOSE CURSOR
                cursor.close()       
                print('item:' , item)
                # RETURN DICTIONARY
                return item
        except Exception as e:
            if cursor is not None:
                # CLOSE CURSOR
                cursor.close()
            # PRINT ERROR
            traceback.print_exc()
            raise e

    def delete_by_id(id):
        cursor = None
        try:
            # CREATING CONNECTION CURSOR
            cursor = mysql.connection.cursor()
            # EXECUTE SELECT BY ID
            cursor.execute(statement_delete_by_id(table, columns), (id,))
            # GET ROW
            row = cursor.fetchone()
            # COMMIT TRANSACTION
            mysql.connection.commit()
            # CLOSE CURSOR
            cursor.close()
        except Exception as e:
            if cursor is not None:
                # CLOSE CURSOR
                cursor.close()
            # PRINT ERROR
            traceback.print_exc()
            raise e

    # PUBLIC LOCAL METHOD
    return {
        'select_all': select_all,
        'insert': insert,
        'update': update,
        'select_by_id': select_by_id,
        'delete_by_id': delete_by_id,
    }