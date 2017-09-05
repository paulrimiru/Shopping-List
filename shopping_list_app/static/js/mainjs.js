$(document).ready(function(){
    $('.parallax').parallax();
    Materialize.updateTextFields();

    $("#password").on("focusout", function (e) {
      if ($(this).val() != $("#confpassword").val()) {
          $("#confpassword").removeClass("valid").addClass("invalid");
      } else {
          $("#confpassword").removeClass("invalid").addClass("valid");
      }
  });
  
  $("#confpassword").on("keyup", function (e) {
      if ($("#password").val() != $(this).val()) {
          $(this).removeClass("valid").addClass("invalid");
      } else {
          $(this).removeClass("invalid").addClass("valid");
      }
  });
  
  });

