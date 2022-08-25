window.onload=function(e){
    let content = document.getElementById('content');
    let arrClassName = [
      'primary',
      'secondary',
      'success',
      'danger',
      'warning',
      'info',
      'light',
      'dark',
    ]

    let elemWrapper = document.createElement('div');
    elemWrapper.setAttribute('style', "padding: 20px;");

    let elemLink = document.createElement('a');
    elemLink.href = 'https://getbootstrap.com/docs/4.0/components/alerts/#additional-content';
    elemLink.textContent = 'https://getbootstrap.com/docs/4.0/components/alerts/#additional-content';
    elemLink.setAttribute('target', "_blank");
    elemWrapper.appendChild(elemLink)

    content.appendChild(elemWrapper);

    for (let i = 0; i < arrClassName.length; i++) {
        let ClassName = arrClassName[i];

        let elemDiv = document.createElement('div');
        elemDiv.classList.add('alert')
        elemDiv.classList.add(`alert-${ClassName}`)
        elemDiv.textContent = `Стиль: ${ClassName}`;
        
        content.appendChild(elemDiv)
       
   };
};
