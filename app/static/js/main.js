function setLocation(city) {
    document.getElementById('location').value = city;
}

async function handleSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    try {
        const response = await fetch('/doctor_consultation', {
            method: 'POST',
            body: formData
        });
        const result = await response.json();

        showToast(result.message, result.success ? 'default' : 'destructive');
        if (result.success) {
            form.reset();
            document.getElementById('date-display').textContent = 'Today';
            document.getElementById('date').value = '';
        }
    } catch (error) {
        showToast('An error occurred. Please try again.', 'destructive');
    }
}

function setupTabs() {
    const tabs = document.querySelectorAll('.tab');
    const contents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));

            tab.classList.add('active');
            const contentId = tab.dataset.tab;
            document.getElementById(contentId).classList.add('active');
        });
    });
}

function openModal(categoryId) {
    const modal = document.getElementById(`modal-${categoryId}`);
    modal.classList.remove('hidden');
}

function closeModal(categoryId) {
    const modal = document.getElementById(`modal-${categoryId}`);
    modal.classList.add('hidden');
}

document.addEventListener('DOMContentLoaded', () => {
    setupTabs();
});