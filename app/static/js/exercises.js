// exercises.js
document.addEventListener('DOMContentLoaded', function() {
    // Tab functionality
    const tabTriggers = document.querySelectorAll('.tab-trigger');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabTriggers.forEach(trigger => {
      trigger.addEventListener('click', function() {
        // Remove active class from all triggers and contents
        tabTriggers.forEach(t => t.classList.remove('active'));
        tabContents.forEach(c => {
          c.classList.remove('active');
          c.classList.add('hidden');
        });
        
        // Add active class to clicked trigger
        this.classList.add('active');
        
        // Show corresponding content
        const tabName = this.getAttribute('data-tab');
        const content = document.getElementById(tabName);
        content.classList.add('active');
        content.classList.remove('hidden');
      });
    });
    
    // Exercise start buttons
    const startButtons = document.querySelectorAll('button');
    startButtons.forEach(button => {
      if (button.textContent.trim() === 'Start Exercise') {
        button.addEventListener('click', function() {
          const exerciseName = this.closest('.bg-white').querySelector('h3').textContent;
          alert(`Starting exercise: ${exerciseName}`);
          // In a real app, this would navigate to the exercise details page or start a video
        });
      }
      
      if (button.textContent.trim() === 'Create My Exercise Plan') {
        button.addEventListener('click', function() {
          alert('This would open the personalized exercise plan creation form');
          // In a real app, this would open a form or navigate to the plan creation page
        });
      }
    });
  });