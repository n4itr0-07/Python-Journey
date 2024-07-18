<h2> E-commerce Database</h2>

<hr>

**Code Functionality:**

This Python script utilizes Faker to generate random user data and inserts it into an e-commerce database created using MySQL. It ensures unique email addresses for each user during the insertion process.

**Step-by-Step Breakdown:**

1. **Imports:**
   - `mysql.connector`: Connects to the MySQL database.
   - `Faker`: Generates random user data.

2. **Database Connection:**
   - Establishes a connection to the MySQL database using your credentials (host, username, password, and database name).

3. **`truncate_string` Function (Optional):**
   - This function truncates strings to a specified length if needed for your database columns. You can remove these calls if truncation is not necessary.

4. **`generate_unique_email` Function:**
   - This function keeps generating email addresses using Faker until a unique one is found. It handles duplicate email errors during insertion.

5. **User Data Generation:**
   - A loop iterates 1000 times (or any desired number of users).
   - Inside the loop:
     - Username, email (using `generate_unique_email`), password, first/last name, phone number, address, city, state, zip code, and country are generated using Faker.

6. **Data Insertion:**
   - An SQL INSERT statement is executed to insert the generated user data into the `Users` table in your MySQL database.

7. **Database Commit and Close:**
   - The database changes are committed.
   - The cursor and database connection are closed.

<hr>

<h3> MySQL Database Code Link</h3>
<b><p> Follow The Given Link For Code Tamplate ⬇️</p></b>
<b><a href="https://github.com/Salik-Seraj/MySQL-Workshop-Projects/blob/main/E-commerce%20Database.sql"> MySQL Database Code Link</a></b>