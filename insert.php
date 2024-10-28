<?php
$username=$_POST['username'];
$username=$_POST['password'];
$username=$_POST['gender'];
$username=$_POST['email'];
$username=$_POST['phoneCode'];
$username=$_POST['phone'];

if(!empty($username)|| !empty($password)|| !empty($gender)||!empty($email)||!empty($phoneCode)||!empty($phone)){
    $host="localhost";
    $dbUsername="root";
    $dbPassword="";
    $dbname="form";
    $conn=new mysqli($host,$dbUsername,$dbPassword,$dbname);
    if(mysqli_connect_error()){
        die('Connect Error('.mysqli_connect_error().')'.mysqli_connect_error());
    }else{
        $SELECT="SELECT email From register Where email=?Limit 1";
        $INSERT="INSERT Into register(username,password,gender,email,phoneCode,phone) values(?,?,?,?,?,?)";
        $stmt=$conn->prepare($SELECT);
        $stmt->bind_param("s",$email);
        $stmt->execute();
        $stmt->bind_result($email);
        $stmt->store_result();
        $rnum=$stmt->num_rows;

        if ($rnum==0) {
            $stmt->close();
            $stmt=$conn->prepare($INSERT);
            $stmt->bind_param("ssssii",$username,$password,$gender,$email,$phoneCode,$phone);
            $stmt->execute();
            echo "New record inserted sucessfully";
        }else{
            echo "Someone already register using this email";
        }
        $stmt->close();
        $conn->close();
    }
}else{
    echo"All field required";
    die();
}
?>