<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>morsecode.fun - juicyguyzer</title>
    <link href="style.css" rel="stylesheet" type="text/css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
  </head>
  <body style="color:white;background:black;">
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark fixed-top">

    <ul class="navbar-nav">
        <a class="navbar-brand" href="./">
        <img src="logo.png" alt="Logo" style="width:40px;">
        </a>
        <li class="nav-item">
        <a class="nav-link" href="keyer.php">Morse Keyer</a>
        </li>
        <li class="nav-item">
        <a class="nav-link" href="translator.php">Morse Translator</a>
        </li>
        <?php
          if(isset($_COOKIE['login'])) {
            echo("<li class='nav-item'>
                    <a class='nav-link' href='profile.php?user=".$_COOKIE['login']."'>Your Profile</a>
                    </li>
                    <li class='nav-item'>
                    <a class='nav-link' href='logout.php'>Log Out</a>
                    </li>
                    <li class='nav-item'>");
            if ($_COOKIE['login'] == "juicy") {
              echo("<a class='nav-link' href='settings.php'>Settings</a>
              <li class='nav-item'>
              <a class='nav-link'><img src='./custompfp/juicy.jpg' width='20' height='20' style='border-radius: 50%;'></img></a>
              </li>");
            } else if ($_COOKIE['login'] == "alilt5") {
                echo("<a class='nav-link' href='settings.php'>Settings</a>
                <li class='nav-item'>
                <a class='nav-link'><img src='./custompfp/alilt5.jpg' width='20' height='20' style='border-radius: 50%;'></img></a>
                </li>");
            } else {
              echo("<a class='nav-link' href='settings.php'>Settings</a>
              <li class='nav-item'>
              <a class='nav-link'><img src='pfp.jpg' width='20' height='20' style='border-radius: 50%;'></img></a>
              </li>");
            }
          } else {
            echo("<li class='nav-item'>
                    <a class='nav-link' href='register.php'>Register</a>
                    </li>
                    <li class='nav-item'>
                    <a class='nav-link' href='login.php'>Log In</a>
                    </li>");
          }
        ?>

    </ul>
    </nav>
    <br>
    <br>
    <br>
    <h1 style="color: white;">Made by juicyguyzer / Ian Park</h1>
    <?php
      if(isset($_COOKIE['login'])) {
        echo("<a href='profile.php?user=".$_COOKIE['login']."'><button>Profile</button></a>
        <a href='keyer.php'><button>Keyer</button></a><a href='logout.php'><button>Log Out</button></a>");
      } else {
        echo("<a href='register.php'><button>Register</button></a><a href='login.php'><button>Log In</button></a>");
      }
    ?>
  </body>
</html>
