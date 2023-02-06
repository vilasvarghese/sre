<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Hello World web application</title>
</head>
<body>
   Hello how are you???? Today is 24th April. Hello Mobileum - wake up!!! subah ho gayi!!
	<h1>Thanks a lot for being so patient through the session!</h1>
    	<form action="ec2Servlet" method="post">
    	<!--Enter AMI: <input type="text" name="ami" size="20">-->
			<input type="submit" value="Create EC2 Instance" />
		</form>
    	<form action="s3Servlet" method="post">
    	<!--Enter AMI: <input type="text" name="ami" size="20">-->
			<input type="submit" value="Create S3 Bucket" />
		</form>
</body>
</html>
