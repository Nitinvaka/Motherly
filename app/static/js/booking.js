
// Handle form submit
document.getElementById('appointmentForm').addEventListener('submit', function(e) {
  e.preventDefault();

  // Show the toast notification
  var toast = document.getElementById('successToast');
  toast.className = "toast show";

  // Hide after 3 seconds
  setTimeout(function() {
    toast.className = toast.className.replace("show", "");
  }, 3000);

  // Reset form if you want
  this.reset();
});