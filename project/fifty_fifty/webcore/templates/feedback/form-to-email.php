<?php
//if "email" variable is filled out, send email
  if (isset($_REQUEST['email']))  {

  //Email information
  $admin_email = "mentoring@fifty50.org.au";
  $email = $_REQUEST['email'];
  $fname = $_REQUEST['firstname']
  $lname = $_REQUEST['lastname']
  $message = $_REQUEST['message'];

  //send email
  mail($admin_email, "$message", "From:" . $email);

  //Email response
  echo "Thank you for contacting us!";
?>
