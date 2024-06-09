use gold_db
go
create or alter proc createsqlserverlessview_gold@viewName nvarchar(100)

as 
begin
decalre @statement varchar(max)
set @statement = N'create or alter view' + @viewname + as

    select *
    from
        openrowset(
            bulk 'https://datalake.dfs.core.windows.net/gold/SalesLT/'
            + @viewName + '/',
            format = 'delta'
        ) as [result]

Exec (@statement)

end

go
