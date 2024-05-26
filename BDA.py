import mysql.connector
#i__Ragav@127.0.0.1:5000
#i__Ragav@127.0.0.1:5000
#jdbc:mysql://127.0.0.1:5000/?user=i__Ragav
def initialize_database():
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=5000,
        user="root",  # Replace with your MySQL username
        password="Kamalesh@000" # Replace wiKth your MySQL password
    )
    c = conn.cursor()

    # Create 'blood_donation' database if it doesn't exist
    c.execute("CREATE DATABASE IF NOT EXISTS blood_donation")
    c.execute("USE blood_donation")

    # Create 'Donor' table
    c.execute('''CREATE TABLE IF NOT EXISTS Donor (
                    Donor_ID INT AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(100),
                    Age INT,
                    Gender VARCHAR(10),
                    Blood_Type VARCHAR(3),
                    Contact_Info VARCHAR(255), 
                    Last_Donation_Date DATE,
                    Medical_History TEXT
                )''')

    # Create 'Recipient' table
    c.execute('''CREATE TABLE IF NOT EXISTS Recipient (
                    Recipient_ID INT AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(100),
                    Age INT,
                    Gender VARCHAR(10),
                    Blood_Type VARCHAR(3),
                    Contact_Info VARCHAR(255),
                    Medical_Condition TEXT,
                    Hospital VARCHAR(255)
                )''')

    # Create 'Blood_Donation' table
    c.execute('''CREATE TABLE IF NOT EXISTS Blood_Donation (
                    Donation_ID INT AUTO_INCREMENT PRIMARY KEY,
                    Donor_ID INT,
                    FOREIGN KEY (Donor_ID) REFERENCES Donor(Donor_ID),
                    Donation_Date DATE,
                    Blood_Type VARCHAR(3),
                    Volume DECIMAL(5, 2)
                )''')

    # Create 'Blood_Inventory' table
    c.execute('''CREATE TABLE IF NOT EXISTS Blood_Inventory (
                    Inventory_ID INT AUTO_INCREMENT PRIMARY KEY,
                    Donation_ID INT UNIQUE,
                    FOREIGN KEY (Donation_ID) REFERENCES Blood_Donation(Donation_ID),
                    Expiry_Date DATE,
                    Storage_Location VARCHAR(255),
                    Quantity_Available INT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS user(
            
                    userName VARCHAR(100),
                    password varchar(100),
                  
                )''')

    # Commit and close connection
    conn.commit()
    conn.close()

# Call the function to initialize the database
initialize_database()
