window.onload=function(e){
    let content = document.getElementById('content');

    for (let i = 1; i < 3; i++) {
        let elemImg = document.createElement('img');
        elemImg.src = `/static/img/admin/favico${i}.jpg`;
        elemImg.alt = 'img';

        let elemDiv = document.createElement('div');

        elemDiv.appendChild(elemImg)
        content.appendChild(elemDiv)
    };
};
