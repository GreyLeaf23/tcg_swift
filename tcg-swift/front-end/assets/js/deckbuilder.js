var totalCountSpan = document.getElementById('totalCount');
var totalCount = 0;
var totalNonTrainersSpan = document.getElementById('totalNonTrainers');
var totalNonTrainersCount = 0;
var totalEnergySpan = document.getElementById('totalEnergy');
var totalEnergyCount = 0;
var totalTrainerSpan = document.getElementById('totalTrainer');
var totalTrainerCount = 0;

// Function to capitalize the first letter of each word, except "ex" and capitalize the letter following a "{"
function capitalizeWordsExceptEx(string) {
    return string.split(/[\s_]+/).map(function(word) {
        if (word.toLowerCase() === "ex") {
            return word.toLowerCase();
        } else if (word.toUpperCase() === "PAF" || word.toUpperCase() === "PAF" || word.toUpperCase() === "PH") {
            return word.toUpperCase();
        } else {
            let capitalizedWord = word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
            // Check if the word has "{" and capitalize the next letter if exists
            let idx = capitalizedWord.indexOf("{");
            if (idx !== -1 && idx + 1 < capitalizedWord.length) {
                capitalizedWord = capitalizedWord.substring(0, idx + 1) + capitalizedWord.charAt(idx + 1).toUpperCase() + capitalizedWord.substring(idx + 2);
            }
            return capitalizedWord;
        }
    }).join(' ');
}

// Function to update the total count and disable buttons if the total count exceeds 60
function updateTotalCount(count) {
    totalCount += count;
    if (totalCount >= 60) {
        totalCount = 60; // Limit total count to 60
        // Disable buttons with class "main"
        var mainButtons = document.querySelectorAll('.main button');
        for (var i = 0; i < mainButtons.length; i++) {
            mainButtons[i].disabled = true;
        }
    }
    totalCountSpan.textContent = 'Total Cards: ' + totalCount;
}

// Function to update the total non-trainers count
function updateTotalNonTrainersCount() {
    var nonTrainersCount = document.querySelectorAll('#counterContainer p:not([id*="TRA-"]):not([id*="energy"])').length;
    totalNonTrainersSpan.textContent = 'Pokémon: ' + nonTrainersCount;
}

// Function to update the total energy cards count
function updateTotalEnergyCount() {
    var energyCount = document.querySelectorAll('#energyContainer p[id*="energy"]').length;
    totalEnergySpan.textContent = 'Energy: ' + energyCount;
}

// Function to update the total energy cards count
function updateTotalTrainerCount() {
    var trainerCount = document.querySelectorAll('#trainersContainer p[id*="TRA-"]').length;
    totalTrainerSpan.textContent = 'Trainer: ' + trainerCount;
}

// Function to increment the counter and create/update the paragraph text
function incrementCount(id) {
    var container = document.getElementById('counterContainer');
    var countParagraph = document.getElementById(id);
    
    if (!countParagraph) {
        // If the paragraph doesn't exist, create it
        countParagraph = document.createElement('p');
        countParagraph.id = id;
        countParagraph.textContent = '1 ' + capitalizeWordsExceptEx(id.replace(/TRA-/g, '').replace(/_/g, ' '));
        container.appendChild(countParagraph);
    } else {
        // If the paragraph already exists and count is less than 4, update its count
        var currentCount = parseInt(countParagraph.textContent.split(' ')[0]);
        if (currentCount < 4 || id.toLowerCase().includes('energy')) {
            countParagraph.textContent = (currentCount + 1) + ' ' + capitalizeWordsExceptEx(id.replace(/TRA-/g, '').replace(/_/g, ' '));
        } else {
            return; // Don't update total count if maximum count reached
        }
    }
    
    // Check if the ID contains "TRA-"
    if (id.includes('TRA-')) {
        // Move the paragraph to the trainers container
        var trainersContainer = document.getElementById('trainersContainer');
        trainersContainer.appendChild(countParagraph);
    }

    // Check if the ID contains "energy"
    if (id.includes('energy')) {
        // Move the paragraph to the energy container
        var energyContainer = document.getElementById('energyContainer');
        energyContainer.appendChild(countParagraph);
    }
    
    // Update total count
    updateTotalCount(1);
    
    // Update total non-trainers count
    updateTotalNonTrainersCount();
    
    // Update total energy cards count
    updateTotalEnergyCount();

    // Update total trainer cards count
    updateTotalTrainerCount();
}



//Clipboard copy
document.getElementById("copyButton").addEventListener("click", function() {
    var textToCopy = document.getElementById("copythis").innerText;
    
    // Create a textarea element to hold the text temporarily
    var textarea = document.createElement("textarea");
    textarea.value = textToCopy;
    document.body.appendChild(textarea);
    
    // Select the text in the textarea
    textarea.select();
    textarea.setSelectionRange(0, 99999); /* For mobile devices */

    // Copy the selected text
    document.execCommand("copy");
    
    // Remove the textarea
    document.body.removeChild(textarea);

    // Optionally, provide some feedback to the user
    alert("Text copied to clipboard: " + textToCopy);
});