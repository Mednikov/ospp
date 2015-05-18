/* Author: Pavel Mednikov (hello@pavelmednikov.com) */
$(document).ready(function () {


  $('a[data-target="uploadImage"]').click(function() {
     console.log("HEY");
  });

  console.log( $("a[data-target='uploadImage']") );

  var projectName = $(".project-name h4").text();
  console.log(projectName);
  $("#id_project option").each(function(){
    // $('this').removeAttr('selected','selected');
    console.log($('this').text());
    // if ( $('this').val = projectName ){
    //   console.log($('this').val+" === OK");
    // } else {
    //   console.log($('this').val+" === Fuck");
    // };
  });



});
