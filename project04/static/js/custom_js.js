    $(document).ready(function(){
        //alert("hello");
        //$("div a").css("color", "red");
        //$("div .caption a").attr("style", "color:red;");
        //$("div a").attr("class", "newClass");
        //$("ul  li:nth-child(2n)").css('color','#8a6d3b');

        $(".jumbotron").fadeIn({
            "duration":400,
            "easing":"easeInBounce",
        });

        $(".btn-primary").click(function(event){
            event.preventDefault();

            //alert("preventing default");
            /*console.log($("div a").css("color"));
            $the_white_color = "rgb(255, 255, 255)"
            if($("div a").css("color") == $the_white_color){
                $("div a").css("color","red");
            } else{
                $("div a").css("color", $the_white_color);
            }*/


            $('h2').fadeOut();
            $('div.thumbnail').fadeIn();

        })

        $(".glyphicon-trash").click(function(event){
            event.preventDefault();
            $(this).parent().fadeToggle();
        })

        $(".glyphicon-off").click(function(event){
            event.preventDefault();
            $(".container h2").fadeToggle("slow",function(){
                $(this).text("Are you going to loggout?");
            }).fadeToggle();
        })
            
    })