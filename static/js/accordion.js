$(function(){
    $(".accordion,.accordion_level2,.accordion_level3").accordion({
        
        change: function(event, ui){
            var clicked = $(this).find('.ui-state-active').attr('id');
            $('#'+clicked).load('/widgets/'+clicked);
        },
        active: false,
        navigation: true,
        collapsible: true,
        autoHeight: false,
        clearStyle: true,
        icons: { "header": "ui-icon-plus", "headerSelected": "ui-icon-minus" } 
    });
    
    $("a", ".accordion").click(function(e) {
        $("#ajax-content").load($(this).attr("href")); });      

    
});