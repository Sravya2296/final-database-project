<!DOCTYPE html>
<html>
<head>
    <title>Edit Employee</title>
</head>
<body>
    <h1>Edit Employee</h1>
    <form action="/update_employee/{{employee[0]}}" method="post">
        Name: <input type="text" name="name" value="{{employee[1]}}"><br>
        Organization ID: <input type="text" name="organization_id" value="{{employee[2]}}"><br>
        <input type="submit" value="Update">
    </form>
</body>
</html>
