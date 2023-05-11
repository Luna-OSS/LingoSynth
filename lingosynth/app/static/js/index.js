function stopRephrasing() {
    rephraseButton.classList.remove('loading');
    textWrapper.classList.remove('loading');   
    rephraseIcon.className = 'ti ti-language'; 
}

function rephrase() {
    if (textBox.classList.contains('loading')) {
        return;
    }

    rephraseButton.classList.add('loading');
    textWrapper.classList.add('loading');
    rephraseIcon.className = 'ti ti-loader-2';

    const data = {
        text: textBox.value
    };

    fetch('/api/rephrase', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'User-Agent': navigator.userAgent
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        textBox.value = data.text;
        stopRephrasing();
    })
    .catch((error) => {
        stopRephrasing();
        console.error('Error:', error);

        popups.innerHTML = '';

        const errorDiv = document.createElement('div');
        errorDiv.className = 'error alert';
        errorDiv.innerText = 'An error occurred. Please try again later.';
        popups.appendChild(errorDiv);

        const closeButton = document.createElement('i');
        closeButton.className = 'ti ti-x';
        closeButton.addEventListener('click', function() {
            errorDiv.remove();
        }
        );
        errorDiv.appendChild(closeButton);
    });
};

document.addEventListener('keydown', function(event) {
    if (event.ctrlKey && event.keyCode === 13) {
        rephrase();
    }
});
