from mysql import connector
class DbConnect:
    def get_connection(self):
        try:
            self.connection=connector.connect(
            host="localhost",
            user="root",
            password="Ansa@123@2004",
            database="puzzle_db"
            )
            print("Database connected successfully")
            return self.connection
        except Exception as e:
            print(e)
class PuzzleManager(DbConnect):
    def get(self):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from puzzles"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for data in records:
                print(data)
        except Exception as e:
            print(e)
    def get_object(self,id=None):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from puzzles where id=%s"
            value=(id,)
            self.cursor.execute(query,value)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from puzzles where id=%s"
            value=(id,)
            self.cursor.execute(query,value)
            record=self.cursor.fetchone()
            print(record)
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            query="insert into puzzles(puzzle_name,puzzle_type,difficulty,pieces) values(%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("New puzzle record added successfully")
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            self.connection=super().get_connection()
            self.cursor=self.connection.cursor()
            query="select * from puzzles where id=%s"
            value=(id,)
            self.cursor.execute(query,value)
            record=self.cursor.fetchone()
            if record!=None:
                self.cursor=self.connection.cursor()
                query="delete from puzzles where id=%s"
                self.cursor.execute(query,value)
                self.connection.commit()
                print("Deleted successfully")
            else:
                print("No record exists")
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s, "
                placeholder=placeholder.rstrip(", ")
                query=f"update puzzles set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Record updated successfully")
            else:
                print("Record not exists")
        except Exception as e:
            print(e)
            

connection_instance=DbConnect()
# connection_instance.get_connection()

puzzle_instance=PuzzleManager()
puzzle_instance.get()
# puzzle_instance.retrieve(1)
# puzzle_instance.post(puzzle_name="word master",puzzle_type="crossword",difficulty="hard",pieces=1)
# puzzle_instance.delete(2)
puzzle_instance.put(id=1,puzzle_name="brain challenge",puzzle_type="sudoku")
        
        
