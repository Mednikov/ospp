/* Author: Pavel Mednikov (hello@pavelmednikov.com) */
$(document).ready(function () {


  var projectId = String(window.location.pathname.match(/\d+/g));

  $("#id_project").each(function(){
    $(this).find('option').removeAttr('selected','selected');
    $(this).val(projectId);
    $(this).parent().attr('hidden','hidden');
  });



});
