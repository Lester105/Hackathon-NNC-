<!doctype html>
<html lang="en">
  <head>
    <title>Address</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel= "stylesheet" href="Registration.css">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300&display=swap" rel="stylesheet">

    <!-- Pyscript Framework -->
    <link rel="stylesheet" href="path/to/pyscript.css" />
    <script defer src="path/to/pyscript.js"></script>

</head>
  <body>
        <div class="header">
            <div class="menu-bar">
            <nav class="navbar navbar-expand-lg navbar-light ">
            <a class="navbar-brand" href="#"><img src="images/nncLogo.png" width= 225px height= 100px class="img-fluid"></a>
            <a class="navbar-brand" href="#"><img src="images/Branding.png" width= 75px height= 100px class="rounded float-left"></a>
            <i class="fa fa-bars"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="index.html">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="Registration.html">Registration</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Update</a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="#">Database</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About</a>
                </li>
                </ul>
            </div>
            </nav>
            </div>
        </div>

    <div class="container">

      <h1>Address</h1>
      <p>Please Indicate the Address</p>

      <hr>
      <label for="Brgy"><b>Barangay (Format: Barangay 15 - Ilawod East) </b></label>
      <input type="text" placeholder="Barangay" name="Barangay" id="Barangay" required>

      <label for="Municipality"><b>Municipality (Format: Legazpi City)</b></label>
      <input type="text" placeholder="Municipality" name="Municipality" id="Municipality" required>

      <label for="Province"><b>Province (Format: Albay)</b></label>
      <input type="text" placeholder="Province" name="Province" id="Province" required>

      <label for="Region"><b>Region (Format: V)</b></label>
      <input type="text" placeholder="Region" name="Region" id="Region" required>

      <hr>

        <a href="Registration3.html"> <button type="submit" class="registerbtn">Next Form (Address)</button></a>
    </div>

  </body>

</html>
