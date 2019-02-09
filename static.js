

$(document).ready(function(){

    

    $("#login").click(function(){

        var user =$ ("#username").val();

        var pwd =$ ("#password").val();

        var pd ={"username":user,"password":pwd};

        $.ajax({

            type:"post",

            url:"http://localhost:8000",

            data:pd,

	    dataType:"text",

	    cache:false,
            success:function(data){

                alert("ok");

            },

	    error:function(){

                alert("error");

            },

        });   

    });

});
