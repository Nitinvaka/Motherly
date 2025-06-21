document.addEventListener('DOMContentLoaded', () => {
    const trigger = document.getElementById('date-trigger');
    const content = document.getElementById('calendar');
    const dateDisplay = document.getElementById('date-display');
    const dateInput = document.getElementById('date');

    trigger.addEventListener('click', () => {
        content.classList.toggle('hidden');
        if (!content.innerHTML) {
            renderCalendar();
        }
    });

    function renderCalendar() {
        const today = new Date();
        const month = today.getMonth();
        const year = today.getFullYear();

        const daysInMonth = new Date(year, month + 1, 0).getDate();
        let html = '<div class="calendar">';
        html += `<div class="calendar-header">${today.toLocaleString('default', { month: 'long' })} ${year}</div>`;
        html += '<div class="calendar-grid">';

        const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        weekdays.forEach(day => {
            html += `<div class="calendar-day-header">${day}</div>`;
        });

        const firstDay = new Date(year, month, 1).getDay();
        for (let i = 0; i < firstDay; i++) {
            html += '<div></div>';
        }

        for (let day = 1; day <= daysInMonth; day++) {
            html += `<button class="calendar-day" data-date="${year}-${month + 1}-${day}">${day}</button>`;
        }

        html += '</div></div>';
        content.innerHTML = html;

        content.querySelectorAll('.calendar-day').forEach(button => {
            button.addEventListener('click', () => {
                const date = button.dataset.date;
                dateInput.value = date;
                dateDisplay.textContent = new Date(date).toLocaleDateString('en-US', {
                    weekday: 'long',
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric'
                });
                content.classList.add('hidden');
            });
        });
    }

    document.addEventListener('click', (e) => {
        if (!trigger.contains(e.target) && !content.contains(e.target)) {
            content.classList.add('hidden');
        }
    });
});