$('document').ready(function(){

$('#search').keyup(function(){
        
$.ajax({
        type:"POST",
        url:"/articles/search/",
        data:{
                
                'search_text':$('#search').val(),
                'csrfmiddlewaretoken':$("input[name=csrfmiddlewwaretoken]").val()
                
                        
                },
                success:searchSuccess,
                dataype:'html'
                });
        });
});
                
function searchSuccess(data,textStatus,jqXHR):
{

        $('#search_results').html(data)
}