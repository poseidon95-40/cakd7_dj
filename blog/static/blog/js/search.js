function searchPost(){
    let searchValue = document.getElementById('search-input').value.trim()
    if (searchValue.length > 1) {
        location.href='/blog/search/'+searchValue+'/'
    }
    else{
        alert('search word('+searchValue+') is too short ')
    }
}

document.getElementById('search-input').addEventListener('keyup', function(event){
    if(event.key === 'Enter'){
        searchPost();
    }
});