function passwordCheck(){
    var password = prompt("Please enter the password.");
    if (password==="ilikepie"){
        window.location="realpage.html";
    } else{
        while(password !=="teste123"){
            password = prompt("Please enter the password.");
        }
        window.location="realpage.html";
    }
}
window.onload=passwordCheck;