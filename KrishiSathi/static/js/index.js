$(document).ready(function(){
    $("#get_users").click(function(){
		 $.ajax({
             url: "http://127.0.0.1:8000/api/users",
             success: function(result){
                 console.log(result[1]);
                $("#jpt").html(result[1]);
             }
		 });
    });
});