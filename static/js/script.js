const outputElement = document.getElementById('prediction-output');
const loadingElement = document.getElementById('loading');
const predictBtn = document.getElementById('predict-btn');

const animatePrediction = (text) => {
    let index = 0;
    outputElement.textContent = '';
    
    const typeWriter = () => {
        if (index < text.length) {
            outputElement.textContent += text[index];
            index++;
            requestAnimationFrame(typeWriter);
        }
    };
    
    requestAnimationFrame(typeWriter);
};

const handlePrediction = async () => {
    const userInput = document.getElementById('user-input').value.trim();
    if (!userInput) return;

    predictBtn.disabled = true;
    outputElement.classList.remove('visible');
    loadingElement.style.display = 'block';

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ input: userInput })
        });

        if (!response.ok) throw new Error('Server responded with error');
        
        const data = await response.json();
        const prediction = data.prediction || "Unable to generate prediction. Please try again.";

        animatePrediction(prediction);
        outputElement.classList.add('visible');
    } catch (error) {
        outputElement.textContent = "⚠️ Connection error. Please check your network and try again.";
        outputElement.classList.add('visible');
        console.error('Prediction error:', error);
    } finally {
        predictBtn.disabled = false;
        loadingElement.style.display = 'none';
    }
};

predictBtn.addEventListener('click', handlePrediction);

// Accessibility enhancements
document.getElementById('user-input').addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') handlePrediction();
});