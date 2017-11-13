
function validEmail()
{
    var email   = document.forms["myForms"]["email1"];
    if( /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value) == false)
    {
        email.focus();
        email.style.borderBottom = "2px solid red";
        return false;
    }
    else
    {
        email.style.border = "1px solid silver"; 
       
    }
}
function changeColor(id)
{
    var id_name= document.forms["myForms"][id];
    id_name.style.border = "1px solid silver";
}

function login(){
    newemail=document.getElementById("email");
    newpassword=document.getElementById("password");
    
    var email1=localStorage.getItem("emaillocal");
    var password1= localStorage.getItem("passwordlocal");
    
    if(newemail.value == email1 && newpassword.value == password1){
        return true;
    }
        else{
            alert("Error: Invalid Email and Password");
            return false;
        }
    
}
