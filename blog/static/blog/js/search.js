function searchPost(){
    let searchValue = document.getElementById('search-input').ariaValueMax.trim()
    if (searchValue.length > 1) {
        location.href='/blog/search/'+searchValue+'/'
    }
    else{
        alert('search word("+searchValue+") is too shrt ')
    }

    document.getElementById('seach-input').addEventListener('keyup', function(event){
        if(event.key === 'Enter'){
            searchPost()
        }
    })
}