$(document).ready(function(){

    if($('#result') != null){
        Read();
    }

  $('#create').on('click', function(){
    $name = $('#name').val();
    
    if($name == ''){
        alert('Please enter a name');
    }
    else{
        $.ajax({
            url: 'create/',
            type: 'POST',
            data: {
                name : $name,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                Read();
                $('#name').val('');
                alert('Successfully created')
            }
        })
    }

  })
    

})




function Read(){
    $.ajax({
        url: 'read/',
        type: 'POST',
        async: false,
        data:{
            res: 1,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('#result').html(response);
        }
    });
}