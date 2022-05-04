<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
  <link href="/css/app.css" rel="stylesheet">
  <style> 
    body {
    background: #d1d5db
    }

    .height {
    height: 100vh
    }

    .form {
    position: relative
    }

    .form .fa-search {
    position: absolute;
    top: 20px;
    left: 20px;
    color: #9ca3af
    }

    .form span {
    position: absolute;
    right: 17px;
    top: 13px;
    padding: 2px;
    border-left: 1px solid #d1d5db
    }

    .left-pan {
    padding-left: 7px
    }

    .left-pan i {
    padding-left: 10px
    }

    .form-input {
    height: 55px;
    text-indent: 33px;
    border-radius: 10px
    }

    .form-input:focus {
    box-shadow: none;
    border: none
    }
  </style>
</head>
<h1>Search Engine</h1>
<div class="container">
    <div class="row height d-flex justify-content-center align-items-center">
        <div class="col-md-6">
            <div class="form"> <i class="fa fa-search"></i> <input type="text" class="form-control form-input" placeholder="Search anything..."> <span class="left-pan"><i class="fa fa-microphone"></i></span> </div>
        </div>
    </div>
</div>
</html>
