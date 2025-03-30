# SkillBridge

SkillBridge is a simple command-line interface (CLI) application that allows users to post and browse job opportunities. It provides a platform for individuals to share short-term or freelance jobs in various categories.

## Features
- **Post a Job**: Users can post jobs with details such as title, description, pay (in USD), contact information, location, category, and date/time.
- **Browse Jobs**: Users can explore available jobs categorized into different industries.
- **Manage Jobs**: Job posters can edit or delete their listings using a unique job ID.
- **MySQL Database**: The program stores job listings in a MySQL database and ensures the database is created if it doesn't exist.

## Installation
### Prerequisites
- Python 3.x
- MySQL Server
- MySQL Connector for Python

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/skillbridge-cli.git
   cd skillbridge-cli
   ```
2. Install MySQL Connector:
   ```sh
   pip install mysql-connector-python
   ```
3. Update database credentials in `skillbridge.py`:
   ```python
   conn = mysql.connector.connect(
       host="localhost",
       user="your_mysql_username",
       password="your_mysql_password"
   )
   ```
4. Run the program:
   ```sh
   python skillbridge.py
   ```

## Usage
1. Run the script and choose an option from the menu:
   - Post a job
   - Browse jobs
   - Manage jobs
   - Exit
2. When posting a job, a unique Job ID will be generated. **Save this ID** to manage your job listing later.
3. Browse jobs by selecting a category to view available opportunities.
4. To manage jobs, enter your saved Job ID to edit or delete a listing.

## Categories
Jobs can be posted in the following categories:
- Writing
- Programming
- Design
- Marketing
- Consulting
- Photography
- Music
- Teaching
- Handyman
- Other

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to submit pull requests or open issues to suggest improvements!

## Contact
For any issues or suggestions, reach out to **your-email@example.com**.

---
Happy Job Posting! 🚀

