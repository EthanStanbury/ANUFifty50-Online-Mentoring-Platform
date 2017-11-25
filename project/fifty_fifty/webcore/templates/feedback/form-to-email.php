<?php
if (isset($_POST['submit'])) {
  $to = 'mentoring@fifty50.org.au';
  $subject = 'Contact Form - New Response';
  $message = 'First Name: ' . $_POST['first_name'] . 'Last Name: ' . $_POST['last_name'] . "\r\n\r\n";
  $message .=  'Email: ' . $_POST['email'] . "\r\n\r\n";
  $message .= 'Message: ' . $_POST['message'];
  $headers = "From: mentoring@fifty50.org.au\r\n";
  $headers .= 'Content-Type: text/plain; charset=utf-8';
  $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
  if ($email){
    $headers .= "\r\nReply-To: $email";
  }
  $success = mail($to, $subject, $message, $headers, '-fmentoring@fifty50.org.au');
}
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="img/logo.png">

    <title>Fifty50 Mentoring Program</title>

    <!-- Bootstrap Core CSS -->
    <link href={% static "MenteePage/vendor/bootstrap/css/bootstrap.min.css" %} rel="stylesheet" type="text/css">

    <!-- Custom Fonts -->
    <link href={% static "MenteePage/vendor/font-awesome/css/font-awesome.min.css" %} rel="stylesheet" type="text/css">

    <!-- Plugin CSS -->
    <link href={% static "MenteePage/vendor/magnific-popup/magnific-popup.css" %} rel="stylesheet" type="text/css">

    <!-- Custom CSS -->
    <link href={% static "MenteePage/css/blog-home.css" %} rel="stylesheet" type="text/css">

    <!-- Theme CSS -->
    <link href={% static "MenteePage/css/creative.min.css" %} rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>

    <![endif]-->


    <style type="text/css">
        .form {
            margin-bottom: 60px;
        }

        input[type=submit] {
            color: white;
            background-color: rgba(246, 139, 35, 1);
            border-radius: 300px;
            padding: 15px 30px;
        }

        input[type=submit]:hover {
            background-color: rgba(189, 24, 34, 1);
        }
    </style>
  </head>
  <body>
    <nav id="mainNav" class="navbar navbar-default navbar-fixed-top">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span> Menu <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand page-scroll" href="../menteelogin.html">
                  Fifty50 Mentoring
                </a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li>
                        {% if request.user.profile.role == 'Mentor' %}
                        <a class="page-scroll" href="../content.html">Training & Content</a>
                        {% else %}
                        <a class="page-scroll" href="../content.html">Content</a>
                        {% endif %}
                    </li>
                    <li>
                        <a class="page-scroll" href="../blog/post_list.html">News & Events</a>
                    </li>

                    <li>
                         {% if request.user.profile.role == 'Mentor' %}
                         <a class="page-scroll" href="../mentor.html">Mentee Details</a>
                        {% else %}
                         <a class="page-scroll" href="../mentor.html">Mentor Details</a>
                        {% endif %}
                    </li>
                    <li>
                        <a class="page-scroll" href="../resources.html">Resources</a>       <!-- login -->
                    </li>
                    <li>
                        <a class="page-scroll" href="../FAQ.html">FAQ & Help</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="feedback_contact.html">Contact Us</a>
                    </li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Me <img src={% static "accounts/img/unnamed.png" %} style="height:25px;width:25px; border-radius: 50%"> <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li>
                                <a class="page-scroll" href="../profile.html">My Profile</a>
                            </li>
                            <li>
                                <a class="page-scroll" href="../settings.html">Settings</a>
                            </li>
                            <li>
                                <a class="page-scroll" href="{% url 'account_logout' %}">Sign Out</a>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container-fluid -->
    </nav>

    <?php if (isset($success) && $success){ ?>
    <h1> Thank You! </h1>
    <p> Your message has been sent! An admin will be in touch soon!</p>
    <?php } else { ?>
    <h1> Oops! </h1>
    <p> There was an error in sending your message. Please contact an admin directly at <a href="mailto:mentoring@fifty50.org.au">mentoring@fifty50.org.au</a>
    </p>
    <?php } ?>

    {% include 'profile_footer.html' %}

    <script>
      function showDiv() {
         document.getElementById('submission_confirmed').style.display = "block";
      }
    </script>

    <!-- jQuery -->
    <script src={% static "MenteePage/vendor/jquery/jquery.min.js" %}></script>

    <!-- Plugin JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
    <script src={% static "MenteePage/vendor/scrollreveal/scrollreveal.min.js" %}></script>
    <script src={% static "MenteePage/vendor/magnific-popup/jquery.magnific-popup.min.js" %}></script>

    <!-- Theme JavaScript -->
    <script src={% static "MenteePage/js/creative.min.js" %}></script>

    <!-- Bootstrap Core JavaScript -->
    <script src={% static "MenteePage/vendor/bootstrap/js/bootstrap.min.js" %}></script>

  </body>
</html>
