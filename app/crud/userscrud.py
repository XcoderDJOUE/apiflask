import MySQLdb

class crudinit():
    """
        description:method to create table users if not exist
    """
    @staticmethod
    def createtable(cursor, conn):
        try:
            cursor.execute(''' 
                    CREATE TABLE IF NOT EXISTS `users` (
                        `id` INT NOT NULL AUTO_INCREMENT , 
                        `email` VARCHAR(255) NOT NULL , 
                        `email_verify` INT NOT NULL DEFAULT '0' , 
                        `verify_time` INT NULL, 
                        `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
                        `updated` TIMESTAMP on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        `password` VARCHAR(255) NOT NULL ,
                        `status` INT NOT NULL DEFAULT '0',
                        PRIMARY KEY (`id`), 
                        UNIQUE (`email`)) ENGINE = InnoDB;
                '''
                )
                
            return True
        except MySQLdb.OperationalError  as inst:
            return inst

    """
        description:method to insert in user
    """ 
    @staticmethod         
    def insertusers(cursor, conn, email, password,email_verify, time):
        try:
            req = 'INSERT INTO users(email,email_verify,verify_time, password) VALUES(%s, %s,%s, %s)'
            value = (email,email_verify, time, password)
            cursor.execute(req,value)
            conn.commit()
            return True
        except MySQLdb.OperationalError  as inst:
            return inst

    """
        description:method to get user by email
    """
    @staticmethod
    def getusers(cursor, conn, email: str):
        try:
            req = 'SELECT * FROM users WHERE email=%s'
            value = (email)
            cursor.execute(req,value)
            columns = [d[0] for d in cursor.description]
            result =  [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result[0]  if result else None
        except MySQLdb.OperationalError  as inst:
            return inst

    """
        description:method to get user by email and code verif
    """
    @staticmethod
    def getusersbycode(cursor, conn, email: str, code: int):
        try:
            req = 'SELECT * FROM users WHERE email=%s AND email_verify=%s'
            value = (email, code)
            cursor.execute(req,value)
            columns = [d[0] for d in cursor.description]
            result =  [dict(zip(columns, row)) for row in cursor.fetchall()]
            return result[0]  if result else None
        except MySQLdb.OperationalError  as inst:
            return inst


    """
        description:method to update and active email verification
    """
    @staticmethod
    def updateuser(cursor, conn, email: str,code: int):
        try:
            req = 'UPDATE users SET status = %s WHERE email=%s AND status=%s AND email_verify=%s'
            value = (1,email, 0, code)
            cursor.execute(req,value)
            conn.commit()
            return True
        except MySQLdb.OperationalError  as inst:
            return inst