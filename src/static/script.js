$( document ).ready(function() {

   $('.overlay').keyup(function () { 
     var text = this.value;
     
     if (text.trim()){
       $(this).parent().find(".name").hide();
       $(this).css("display","block");
     }else{
       $(this).attr("style","");  $(this).parent().find(".name").attr("style",""); 
     }
   }); 
  
  
});