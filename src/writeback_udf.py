import fabric.functions as fn
udf = fn.UserDataFunctions()

@udf.connection(argName="sqlDB", alias="ControllingData")
@udf.function() 
def write_customer_action_plan(sqlDB: fn.FabricSqlConnection, customerId: str, actionPlanText: str) -> str: 
    if len(actionPlanText) > 500 or len(actionPlanText) == 0:
        raise fn.UserThrownError("Komentarz jest pusty lub za długi (max 500 znaków).", {"Text:": actionPlanText})
        
    connection = sqlDB.connect() 
    cursor = connection.cursor() 
    cursor.execute("INSERT INTO [dbo].[CustomerActionPlans] (CustomerID, ActionPlanText) VALUES (?, ?)", (customerId, actionPlanText)) 
    connection.commit() 
    cursor.close() 
    connection.close()  
    return f"Dodano komentarz dla klienta {customerId}."
