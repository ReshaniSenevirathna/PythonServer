<html> <head> <title>Date and Time </title> 
 
 </head> 
 
<body> The program will display the current year, month, date hour, minute, and second.<br> 
 
 <script language="javascript"> 
 
 
 Displaying a Date object  now = new Date();  /* Getting and Displaying the year, month, date, hour, minute, and second*/ 
 
document.write(now.getFullYear()+"Year"); 

document.write(now.getMonth()+1,"Month",now.getDate(),"date");  

document.write(now.getHours(),"hour",now.getMinutes(),"minutes");

document.write(now.getSeconds(),"seconds");


</script>
</body>
</html>