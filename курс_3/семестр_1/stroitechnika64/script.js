document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('callback-form');
    const popup = document.getElementById('popup-form');
    const openFormBtn = document.getElementById('open-form');
    const closeFormBtn = document.getElementById('close-btn');

    openFormBtn.addEventListener('click', () => {
        popup.style.display = 'flex';
    });

    closeFormBtn.addEventListener('click', () => {
        popup.style.display = 'none';
    });

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(form);

        try {
            await fetch('http://127.0.0.1:5000/save', {
                method: 'POST',
                body: formData,
            });
            alert('Ваш запрос успешно отправлен!');
        } catch (error) {
            alert('Ошибка отправки данных!');
        }
    });
});
