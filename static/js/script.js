/* script.js */
async function handlePrediction() {
    const inputData = document.getElementById('user-input').value;
    updatePredictionOutput("🌟 Generating prediction...");

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ input: inputData })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }

        const result = await response.json();

        if (result && result.prediction) {
            updatePredictionOutput(result.prediction);
        } else {
            updatePredictionOutput("⚠️ Prediction failed. No response from the model.");
        }
    } catch (error) {
        console.error('Error:', error);
        updatePredictionOutput("⚠️ Error retrieving prediction. Please try again later.");
    }
}

function updatePredictionOutput(prediction) {
    document.getElementById('prediction-output').textContent = prediction;
}
