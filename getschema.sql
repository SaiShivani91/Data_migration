select
s.name as SchemaName,
t.name as TableName
from sys.tables tablesinner join sys.schemas s
on t.schema_id = s.schema_id
where s.name = 'SalesLT';