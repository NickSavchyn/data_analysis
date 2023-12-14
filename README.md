# CRM System Analytics

This GitHub repository contains SQL queries and instructions to analyze data from a Customer Relationship Management (CRM) system. The provided SQL query addresses a specific task related to CRM operations, and the results include valuable insights for business analytics.

## **Task Description**

The task involves constructing an SQL query to extract key metrics from a CRM system database. The desired output includes information about deals, contacts, engagements, and stages. The metrics to be included in the output are related to the pipeline, product, stage label, creation date, contact information, call statistics, and time metrics.

## **Database Schema**

The CRM system consists of the following tables:

- **Deals:** Primary table containing information about CRM operations.
- **Contacts:** Table containing client information.
- **Engagements:** Table storing data about employee actions in the CRM system.
- **Stages:** Table with data about operation stages and funnels.
- **Associations:** Table for managing relationships between other tables.

## **Columns in the Output**

The SQL query produces a table with the following columns:

- **pipeline**
- **product**
- **stage_label**
- **deals.created_year_and_month**
- **contacts.email**
- **country**
- **city**
- **full_name** (combination of first_name and last_name)
- **calls_number** (count of calls from engagements)
- **mean_calls_duration_sec** (median time of calls duration)
- **days_to_meet** (median time in days from created_at of Deals till created_at of Engagements)

## **How to Use**

1. Clone this repository to your local machine.
2. Connect to your CRM database using a SQL client.
3. Execute the provided SQL query in your SQL client.

Make sure to adjust the query if your database schema or naming conventions differ from the provided schema.

## **Dependencies**

This project assumes a MySQL-compatible database. Adjustments may be necessary for compatibility with other database systems.

## **Contributors**

- [Your Name]

Feel free to contribute by forking the repository and submitting pull requests with improvements or additional features. Issues can be reported on the GitHub repository for bug fixes or enhancements.

Happy analyzing!
