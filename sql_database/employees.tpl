<!DOCTYPE html>
<html>
<head>
    <title>Employees</title>
</head>
<body>
    <h1>Employees</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Organization ID</th>
            <th>Actions</th>
        </tr>
        % for employee in employees:
        <tr>
            <td>{{employee[0]}}</td>
            <td>{{employee[1]}}</td>
            <td>{{employee[2]}}</td>
            <td>
                <a href="/edit_employee/{{employee[0]}}">Edit</a>
                <a href="/delete_employee/{{employee[0]}}">Delete</a>
            </td>
        </tr>
        % end
    </table>

    <h2>Add Employee</h2>
    <form action="/add_employee" method="post">
        Name: <input type="text" name="name"><br>
        Organization ID: <input type="text" name="organization_id"><br>
        <input type="submit" value="Add">
    </form>
</body>
</html>
