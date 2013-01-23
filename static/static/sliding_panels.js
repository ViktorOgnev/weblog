
var panelWidth = 0;
var prevIndex = -1;

$(document).ready(function(){
    
    window.panelWidth = $('.sp').width();
    
    $('.panel_container .panel').each(function(index){
        
        $(this).css({'width':window.panelWidth+'px', 
                     'left':(index*window.panelWidth)+'px'});
        $('.sp .panels').css('width', (index+1)*window.panelWidth+'px');
    });
    
    $('.sp .tabs span').each(function(){
        $(this).click(function(){
            
            var currIndex = $(this).index();
            $(this).addClass('selected');
            if ((currIndex != prevIndex)&&(window.prevIndex >= 0)) {
                $('.sp .tabs span:nth-child('+(prevIndex+1)+')').removeClass('selected');
                
            }
            window.prevIndex = currIndex;
            changePanels( currIndex );
        });
    });
});

function changePanels(newIndex){
    
    var newPanelPosition = (window.panelWidth*newIndex)* -1;
    var newPanelHeight = $('.sp .panel:nth-child('+(newIndex+1)+')'
                           ).find('.panel_content').height()+15;
    
    $('.sp .panels').animate({left:newPanelPosition}, 500);
    $('.sp .panel_container').animate({height:newPanelHeight}, 500);
    
}