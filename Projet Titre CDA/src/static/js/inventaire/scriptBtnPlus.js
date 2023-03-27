    const btn = document.querySelector('#add-counter-btn');
    btn.addEventListener('click', () => {
        const articleId = {{ object.id }};
        fetch(`/update-counter/${articleId}`).then(response => {
            response.json().then(data => {
                document.querySelector('#counter').textContent = data.counter;
            });
        });
    });

    document.getElementById("increment-counter").addEventListener("click", function() {
        const articleId = "{{ article.id }}";
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "{% url 'increment_counter' %}", true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange = function() {
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                const response = JSON.parse(xhr.responseText);
                document.querySelector("p").textContent = `Nombre de vues: ${response.counter}`;
            }
        };
        xhr.send(`article_id=${articleId}`);
    });