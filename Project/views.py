from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import mysql.connector as sql
from django.contrib import messages

def index(request):
    if request.method == "POST":
        # Connect to the database
        m = sql.connect(host="localhost", user="root", passwd="aRYAN5505", database='PWP_Project')
        cursor = m.cursor()

        # Get the POST data
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        uname = request.POST.get('uname', '')
        birthdate = request.POST.get('birthdate', '')
        mobile = request.POST.get('mobile', '')
        email = request.POST.get('email', '')
        password = request.POST.get('pass', '')  # Change this to 'pass' to match the form

        # SQL query to insert user data into the database
        query = """INSERT INTO user_details (First_Name, Last_Name, User_Name, Birthdate, Mobile, Email, Password) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (fname, lname, uname, birthdate, mobile, email, password)
        
        # Execute the query
        cursor.execute(query, values)

        # Commit the changes to the database
        m.commit()
        cursor.close()
        m.close()
        return redirect('index')    

    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def salon(request):
    return render(request, 'salon.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    if not request.session.get('log_in'):
        return redirect('index')

    username = request.session.get('uname')
    m = sql.connect(host="localhost", user="root", passwd="aRYAN5505", database='PWP_Project')
    cursor = m.cursor()
    query = "SELECT First_Name, Last_Name, User_Name, Birthdate, Mobile, Email FROM user_details WHERE User_Name=%s"
    cursor.execute(query, (username,))
    user_data = cursor.fetchone()
    cursor.close()
    m.close()

    if user_data:
        request.session['first_name'] = user_data[0]
        request.session['last_name'] = user_data[1]
        request.session['username'] = user_data[2]
        request.session['birthdate'] = user_data[3]
        request.session['mobile'] = user_data[4]
        request.session['email'] = user_data[5]
    else:
        return redirect('index')  # Redirect if no user found

    return render(request, 'profile.html')

def temp(request):
    return render(request, 'temp.html')

def logout(request):
    request.session.flush()
    return redirect('index')

def update(request):
    return render(request,'update.html')



def updateDetails(request):
    # Ensure the request is POST
    if request.method == 'POST':
        # Retrieve session and form data
        uname = request.session.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        birthdate = request.POST.get('birthdate')

        print(f"Received data: {uname}, {first_name}, {last_name}, {email}, {mobile}, {birthdate}")

        # Establish connection to MySQL
        try:
            connection = sql.connect(
                host='localhost',  
                user='root',  
                password='aRYAN5505',  
                database='PWP_Project' 
            )

            cursor = connection.cursor()

            # Update query
            update_query = """
                UPDATE user_details 
                SET First_Name = %s, Last_Name = %s, Email = %s, Mobile = %s, Birthdate = %s 
                WHERE User_Name = %s
            """
            print(f"Executing query: {update_query}")    

            # Execute the update query with form data
            cursor.execute(update_query, (first_name, last_name, email, mobile, birthdate, uname))

            # Commit the transaction
            connection.commit()

            # Update session variables
            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            request.session['email'] = email
            request.session['mobile'] = mobile
            request.session['birthdate'] = birthdate

            # Add a success message to the request
            messages.success(request, 'User details updated successfully!')

            # Redirect with a success parameter
            return redirect('/profile?success=true')

        except sql.Error as e:
            # Log any errors and show a message to the user
            print(f"Error connecting to MySQL: {e}")
            messages.error(request, 'Failed to update user details.')

        finally:
            # Close the cursor and connection if they are open
            if connection.is_connected():
                cursor.close()
                connection.close()

    return redirect('profile')

def delete_user(request):
    # Get the username from the session
    uname = request.session.get('username')

    # Connect to the MySQL database
    try:
        connection = sql.connect(
            host='localhost',
            user='root',  # Your MySQL username
            password='aRYAN5505',  # Your MySQL password
            database='PWP_Project'  # Your database name
        )
        cursor = connection.cursor()

        # Delete query
        delete_query = "DELETE FROM user_details WHERE User_Name = %s"
        cursor.execute(delete_query, (uname,))
        connection.commit()

        # Log the user out
        logout(request)

        # Remove session variables
        request.session.flush()

        # Redirect to the home page with a success parameter
        return redirect('/?success=true')

    except sql.Error as e:
        print(f"Error: {e}")
        # Redirect to the home page with an error parameter
        return redirect('/?error=true')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def loginaction(request):
    if request.method == "POST":
        # Connect to the database
        m = sql.connect(host="localhost", user="root", passwd="aRYAN5505", database='PWP_Project')
        cursor = m.cursor()

        # Get POST data (username and password)
        uname = request.POST.get('uname', '')
        password = request.POST.get('password', '')

        # Execute query to find matching user
        query = "SELECT * FROM user_details WHERE User_Name=%s AND Password=%s"
        cursor.execute(query, (uname, password))
        user = cursor.fetchall()  # Fetch all record

        if user:
            cursor.close()
            m.close()
            request.session['log_in'] = True
            request.session['uname'] = uname
            
            # Redirect to home page
            return redirect('index')
        else:
            cursor.close()
            m.close()
            request.session['log_in'] = False
            
            # Redirect to home page with error message
            return redirect('/?error_login=true')  # Pass error parameter in the URL

    return redirect('index')  # Redirect to home if the request is not POST



def contact_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        services = request.POST.get('services')
        message = request.POST.get('message')

        # Connect to the database
        try:
            connection = sql.connect(
                host='localhost',
                user='root',
                password='aRYAN5505',
                database='PWP_Project'
            )
            cursor = connection.cursor()

            # Insert query
            insert_query = """
            INSERT INTO customer_contacts (name, number, email, services, message)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (name, number, email, services, message))

            # Commit the transaction
            connection.commit()

            # Redirect to the contact page with success parameter
            return redirect('/contact?success=true')

        except sql.Error as e:
            print(f"Error connecting to MySQL: {e}")
            # Redirect to the contact page with error parameter
            return redirect('/contact?error=true')

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    return render(request, 'contact.html')  # Render the contact form if GET request
