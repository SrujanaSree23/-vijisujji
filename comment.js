// script.js
document.getElementById('suggestionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting normally

    // Get the value from the textarea
    const suggestionInput = document.getElementById('suggestionInput');
    const suggestion = suggestionInput.value;

    // Create a new list item for the suggestion
    const li = document.createElement('li');
    li.textContent = suggestion;

    // Append the new suggestion to the suggestion list
    document.getElementById('suggestions').appendChild(li);

    // Clear the textarea
    suggestionInput.value = '';
});