Team: 404 Name Not Found
----------
<b>Task 1:</b> flag{you_should_have_solved_this_in_ruby}<br/>
The script is located in task1 folder, named t1.py<br/>
![script](task1/)<br/><br/>
Task 2: 

Task 3: using BURP suite, we intercepted POST package after email verification at signup, editted to include the xss script then forward the editted POST package to server<br/>
![intercepted POST](task3/xssattack.png)<br/><br/>
After that we stopped intercepting and received the flag confirmation, which returned correct on Proving Ground <br/>
![flag](task3/flagconfirmation.png)
