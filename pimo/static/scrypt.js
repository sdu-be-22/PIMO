// showpassword method
function showpassword(){
    if (document.getElementById("password").type=="password"){
        document.getElementById("password").type="text";
    }else document.getElementById("password").type="password";

}
function signupp(){  
    var pw = document.getElementById("password").value;  
    //check empty password field  
    if(pw == "") {  
       document.getElementById("message").innerHTML = "**Fill the password please!";  
       return false;  
    }  
     
   //minimum password length validation  
    if(pw.length < 8) {  
       document.getElementById("message").innerHTML = "**Password length must be atleast 8 characters";  
       document.getElementById("message").style = font
       return false;  
    }  
    
  //maximum length of password validation  
    if(pw.length > 15) {  
       document.getElementById("message").innerHTML = "**Password length must not exceed 15 characters";  
       return false;  
    } else {  
       alert("Password is correct");  
       document.location.href = "homePage.html";
    }  
          }
      
      var day=new Date().getDate();
      var month =new Date().getMonth()+1;
      var year =new Date().getFullYear();
      if(day<10){
          day="0"+day;
      }
      document.getElementById("date").max=year+"-"+month+"-0"+day;