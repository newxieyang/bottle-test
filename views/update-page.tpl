% include toolbar
<div id="showUserInfo" style="width:300px; float:left;margin:5px;">
        userinfo:</br>
        username:{{item[0]}}<br>
        password:{{item[1]}}<br>
        phone:{{item[3]}}<br>
        email:{{item[2]}}<br>
	address:{{item[4]}}<br>
</div>
<div id="changeUserInfo" style="width:350px; float:left;margin:5px;">
	<form method="post" action="/updateUser">
        please enter info you want change:<br/>
        username:{{item[0]}}
	<input type="hidden" value={{item[0]}} name="username" /><br>
        password:<input type="text" value={{item[1]}} name="pwd" /><br>
        phone:<input type="text" value={{item[3]}} name="phone" /><br>
        email:<input type="text" value={{item[2]}} name="email" /><br>
        address:<input type="text" value={{item[4]}} name="address" /><br>
	<input type="submit">
	</form>
</div>


