import sqlite3

class Conecction:
    def __init__(self) -> None:
        try:
            self.conn = sqlite3.connect('database.db')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
    def ExecuteQueryAsync(self,query:str,params:tuple):
        try:
            self.cursor.execute(query,params)
            self.conn.commit()
            return {"message":"comandos ejecutados correctamente","status": True}
        except Exception as e:
            self.cursor.rollback()
            return {"message":f"{e}","status": False}
        finally:
            self.conn.close()
    def ListQueryAsync(self,query:str):
        try:
            data = self.cursor.execute(query).fetchall()
            return data
        except Exception as e:
            return f'{e}'
        finally:
            self.conn.close()
