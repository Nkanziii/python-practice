class QueryBuilder:
    def __init__(self):
        self._select = ""
        self._from = ""
        self._where = ""

    def select(self, column: str):
        self._select = column
        return self

    def table_from(self, table: str):
        self._from = table
        return self

    def where(self, where: str):
        self._where = where
        return self

    def build(self):
        return f"SELECT {self._select} FROM {self._from} WHERE {self._where}"

query = QueryBuilder().select("name").table_from("users").where("age > 18").build()
print(query)