// Custom JavaScript for the base.js template

// Update current date and time
setInterval(function () {
    var now = new Date();
    var dateTimeString = now.toLocaleString();
    document.getElementById('currentDateTime').textContent = dateTimeString;
}, 1000);
