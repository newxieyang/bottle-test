% include toolbar
<table>
	<tr>
		<td>id</td>
		<td>username</td>
		<td>phone</td>
		<td>email</td>
		<td>address</td>
		<td>delete</td>
	</tr>
	% for item in items:
	<tr>
		<td>{{item[0]}}</td>
		<td>{{item[1]}}</td>
		<td>{{item[2]}}</td>
		<td>{{item[3]}}</td>
		<td>{{item[4]}}</td>
		<td><input type="button" value="delete" onclick="deleteUser({{item[0]}})"/></td>
	</tr>
	%end

</table>

<script src="/static/js/jquery.js"></script>
<script >
	function deleteUser(id){
		$.ajax({
			type: "POST",
			url: "/deleteUser",
			data:{"id":id},
			success: function(response){
				alert(response);
				window.location.reload();
			},
			error: function(error){
                    		alert('Error: ' + error);
                    	}
        	});
	}
</script>


