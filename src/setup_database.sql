-- DDL for the Fabric SQL Database Writeback Table
-- Includes audit fields (CreatedAt, CreatedBy) for enterprise governance

CREATE TABLE [dbo].[CustomerActionPlans] (
    ActionPlanID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID NVARCHAR(50) NOT NULL,
    ActionPlanText NVARCHAR(500) NOT NULL,
    CreatedAt DATETIME2 DEFAULT CURRENT_TIMESTAMP,
    CreatedBy NVARCHAR(100) DEFAULT SYSTEM_USER
);
