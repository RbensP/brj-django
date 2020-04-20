jQuery(document).ready(function($){
    let url;
    $('.date').click(function(){
        url = this.dataset.url  
        console.log(url)
    });

    $('#confirm').click(function(){
        window.location.replace(url);
    });

    setTimeout(function(){
        $('#message').fadeOut('slow');
    }, 3000);
});