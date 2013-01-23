$(document).ready(function () {
	$("#nav li a").click(function () {
		
		$("#ajax-content").empty().append("<div id='loading'><img src='/static/images/loading.gif' alt='Loading' /></div>");
		$("#nav li a").removeClass('current');
		$(this).addClass('current');
		
		$.ajax({
			url : this.getAttribute('href'),
			success : function (html) {
				$("#ajax-content").empty().append(html);
			}
		}); 
		return false;
	});
	
	$("#ajax-content").empty().append("<div id='loading'><img src='/static/images/loading.gif' alt='Loading' /></div>");
	$.ajax({
		url : "{% url 'coltrane_entry_archive_index' %}",
		success : function (html) {
			$("#ajax-content").empty().append(html);
		}
	});
});




