function goSearch() {
    let title = document.getElementById('menu__search_input').value;
    if (title != null && title != "")
        document.location.href = document.location.origin + `/search/?title=${encodeURI(title)}`;
}

window.addEventListener('load', function(e) {
    $('#menu__search_input')[0].addEventListener('keypress',
            function(e) {
                if (e.key == 'Enter') goSearch();
            }
    );
});

